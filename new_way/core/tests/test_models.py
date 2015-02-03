from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from new_way.core.models import Customer, Employee, Occupation, Address, \
    Dealership, Make, Model, Vehicle, Accessory, Kit, KitDetail, \
    Ordered, Kiosk, Store


class CustomerTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            address=u'Avenida Engenheiro Eusébio Stevaux',
            address_number=100,
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )
        self.obj = Customer(
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31',
            email='regis@example.com',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=self.address
        )
        # CPF válido: 33322211169, 55566678963

    def test_create(self):
        """
        Customer must have first_name, last_name, cpf, birthday, email,
        phone, cell, address, complement, district, city, uf, cep
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Customer must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    # def test_str(self):
    #     self.assertEqual(u'da Silva, Regis', u(self.obj))


class CustomerUniqueTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            address=u'Avenida Engenheiro Eusébio Stevaux',
            address_number=100,
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )
        ''' Create a first entry to force the collision '''
        Customer.objects.create(
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31',
            email='regis@email.com',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=self.address
        )

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Customer(
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31',
            email='regis@example.com',
            phone='11-2600-2500',
            cell='11-98700-0000',
            address=self.address
        )
        self.assertRaises(IntegrityError, s.save)


# class EmployeeTest(TestCase):

#     def setUp(self):
#         self.address = Address.objects.create(
#             address=u'Avenida Engenheiro Eusébio Stevaux',
#             address_number=100,
#             complement='Bloco A',
#             district='Jurubatuba',
#             city=u'São Paulo',
#             uf='SP',
#             cep='04696000'
#         )
#         self.occupation = Occupation.objects.create(
#             occupation='Vendedor'
#         )
#         self.dealership = Dealership.objects.create(
#             dealership='Caoa',
#             address=self.address,
#             phone1='1234-0000',
#             phone2='1234-0001',
#             phone3='1234-0002'
#         )
#         self.obj = Employee(
#             first_name=u'José',
#             last_name='Aciole',
#             cpf='55566678963',
#             birthday='1981-03-01',
#             email='aciole@example.com',
#             phone='11-2800-2500',
#             cell='11-98800-0000',
#             address=self.address,
#             occupation=self.occupation,
#             dealership=self.dealership,
#             comissioned='True',
#             comission=180.5
#         )

#     def test_create(self):
#         """
#         Employee must have first_name, last_name, cpf, birthday, email,
#         phone, cell, address, complement, district, city, uf, cep
#         """
#         self.obj.save()
#         self.assertEqual(1, self.obj.pk)

#     def test_has_created_at(self):
#         'Employee must have automatic created_at'
#         self.obj.save()
#         self.assertIsInstance(self.obj.created_at, datetime)

# TODO: Dealership and DealershipDetail test...

class MakeTest(TestCase):

    def setUp(self):
        self.make = Make.objects.create(
            make='BMW'
        )

    def test_create(self):
        self.assertEqual(1, self.make.pk)


class ModelTest(TestCase):

    def setUp(self):
        self.make = Make.objects.create(
            make='BMW'
        )
        self.obj = Model(
            make=self.make,
            model='X6 M'
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)


class VehicleTest(TestCase):

    def setUp(self):
        self.make = Make.objects.create(
            make='BMW'
        )
        self.model = Model.objects.create(
            make=self.make,
            model='X6 M'
        )
        self.kit = Kit.objects.create(
            kit='video'
        )
        self.obj = Vehicle(
            model=self.model,
            vehicle='X6 M sDrive 35i RWD 4dr Sports Activity Coupe',
            color='black',
            year_of_manufacture=2015,
            engine_power=180,
            fueltype='d',
            transmissiontype='a',
            wheel='disco',
            tire='leve',
            performance='180',
            trunk='frontal',
            price=459950,
            kit_fabric=self.kit,
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)


class AccessoryTest(TestCase):

    def setUp(self):
        self.accessory = Accessory.objects.create(
            accessory='Blue-Ray',
            price_accessory=1200,
        )

    def test_create(self):
        self.assertEqual(1, self.accessory.pk)


class KitTest(TestCase):

    def setUp(self):
        self.kit = Kit.objects.create(
            kit='video'
        )

    def test_create(self):
        self.assertEqual(1, self.kit.pk)


class KitDetailTest(TestCase):

    def setUp(self):
        self.kit = Kit.objects.create(
            kit='video'
        )
        self.accessory = Accessory.objects.create(
            accessory='Blue-Ray',
            price_accessory=1200,
        )
        self.obj = KitDetail(
            kit=self.kit,
            accessory=self.accessory,
            quantity_accessory=2,
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)


class StoreTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            address=u'Avenida Engenheiro Eusébio Stevaux',
            address_number=100,
            complement='Bloco A',
            district='Jurubatuba',
            city=u'São Paulo',
            uf='SP',
            cep='04696000'
        )

        self.obj = Store(
            store='Caoa',
            address=self.address,
        )

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.pk)


class KioskTest(TestCase):

    def setUp(self):
        self.kiosk = Kiosk.objects.create(
            kiosk='Shopping SP Market',
            store_id=1,  # na verdade deveria criar address e store novamente
        )

    def test_create(self):
        self.assertEqual(1, self.kiosk.pk)


class OrderedTest(TestCase):

    def setUp(self):
        self.ordered = Ordered.objects.create(
            customer_id=1,
            employee_id=1,
            vehicle_id=1,
            kit_optional_id=1,
            dealership_id=1,
            kiosk_id=1,
            status='p',
        )

    def test_create(self):
        self.assertEqual(1, self.ordered.pk)

    def test_has_created_at(self):
        'Ordered must have automatic created_at'
        self.ordered.save()
        self.assertIsInstance(self.ordered.created_at, datetime)
