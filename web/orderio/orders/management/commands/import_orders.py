from xml.etree import ElementTree

from django.core.management.base import BaseCommand, CommandError
import xmltodict

from orders.serializers import (
    ProductSerializer, PaymentSerializer, BillingAddressSerializer,
    TrackingSerializer, OrderDetailsSerializer
)


def normalize_data(data: dict):
    """
    Normalize products list for json format.
    When there is only one element, it defaults to a dict instead of list.
    """
    products = data["cart"]["products"].pop("product")
    data["cart"]["products"] = products if isinstance(products, list) else [products]
    return data


def get_saved_obj(data, serializer):
    ser = serializer(data=data)
    ser.is_valid(raise_exception=True)
    return ser.save()


def create_order_related_models(
        order,
        payment: dict,
        billing_address: dict,
        tracking: dict,
        products: list,
):
    order.order_payment = get_saved_obj(payment, PaymentSerializer)
    order.billing_address = get_saved_obj(billing_address, BillingAddressSerializer)
    order.tracking_informations = get_saved_obj(tracking, TrackingSerializer)
    order.products.set([
        get_saved_obj(product, ProductSerializer) for product in products
    ])

    order.save()


def create_order(data: dict):
    # Create order
    order = get_saved_obj(data, OrderDetailsSerializer)

    # Create order related models
    create_order_related_models(
        order,
        payment=data["order_payment"],
        billing_address=data["billing_address"],
        tracking=data["tracking_informations"],
        products=data["cart"]["products"],
    )


def transform_xml_file_content_to_dict(file):
    tree = ElementTree.parse(file)
    root = tree.getroot()
    string_xml = ElementTree.tostring(root, encoding="utf-8", method="xml")
    return dict(xmltodict.parse(string_xml))


class Command(BaseCommand):
    help = "Import orders from XML file."

    def add_arguments(self, parser):
        parser.add_argument("file", nargs=1, type=str)

    def handle(self, *args, **options):
        print("Starting import...")
        data_import = transform_xml_file_content_to_dict(options["file"][0])

        for order in data_import["statistics"]["orders"]["order"]:
            normalize_data(order)
            create_order(data=order)

        print("Imported orders successfully!")
