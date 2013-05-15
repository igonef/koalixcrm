# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("accounting", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding field 'Tax.accountActiva'
        db.add_column('crm_tax', 'accountActiva',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='db_relaccountactiva', null=True, to=orm['accounting.Account']),
                      keep_default=False)

        # Adding field 'Tax.accountPassiva'
        db.add_column('crm_tax', 'accountPassiva',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='db_relaccountpassiva', null=True, to=orm['accounting.Account']),
                      keep_default=False)

        # Adding field 'Product.accoutingProductCategorie'
        db.add_column('crm_product', 'accoutingProductCategorie',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.ProductCategorie'], null=True, blank='True'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tax.accountActiva'
        db.delete_column('crm_tax', 'accountActiva_id')

        # Deleting field 'Tax.accountPassiva'
        db.delete_column('crm_tax', 'accountPassiva_id')

        # Deleting field 'Product.accoutingProductCategorie'
        db.delete_column('crm_product', 'accoutingProductCategorie_id')


    models = {
        'accounting.account': {
            'Meta': {'ordering': "['accountNumber']", 'object_name': 'Account'},
            'accountNumber': ('django.db.models.fields.IntegerField', [], {}),
            'accountType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isACustomerPaymentAccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isProductInventoryActiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopeninterestaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopenreliabilitiesaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'originalAmount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'accounting.productcategorie': {
            'Meta': {'object_name': 'ProductCategorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lossAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_loss_account'", 'to': "orm['accounting.Account']"}),
            'profitAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_profit_account'", 'to': "orm['accounting.Account']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'crm.contract': {
            'Meta': {'object_name': 'Contract'},
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'defaultSupplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Supplier']", 'null': 'True', 'blank': 'True'}),
            'defaultcurrency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Currency']"}),
            'defaultcustomer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Customer']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_contractlstmodified'", 'to': "orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relcontractstaff'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'crm.currency': {
            'Meta': {'object_name': 'Currency'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rounding': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'shortName': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'crm.customer': {
            'Meta': {'object_name': 'Customer', '_ormbases': ['crm.Contact']},
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'defaultCustomerBillingCycle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.CustomerBillingCycle']"}),
            'ismemberof': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['crm.CustomerGroup']", 'null': 'True', 'blank': 'True'})
        },
        'crm.customerbillingcycle': {
            'Meta': {'object_name': 'CustomerBillingCycle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'timeToPaymentDate': ('django.db.models.fields.IntegerField', [], {})
        },
        'crm.customergroup': {
            'Meta': {'object_name': 'CustomerGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'crm.customergrouptransform': {
            'Meta': {'object_name': 'CustomerGroupTransform'},
            'factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fromCustomerGroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromfromcustomergroup'", 'to': "orm['crm.CustomerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Product']"}),
            'toCustomerGroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromtocustomergroup'", 'to': "orm['crm.CustomerGroup']"})
        },
        'crm.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.emailaddressforcontact': {
            'Meta': {'object_name': 'EmailAddressForContact', '_ormbases': ['crm.EmailAddress']},
            'emailaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.EmailAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.emailaddressforcontract': {
            'Meta': {'object_name': 'EmailAddressForContract', '_ormbases': ['crm.EmailAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contract']"}),
            'emailaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.EmailAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.emailaddressforpurchaseorder': {
            'Meta': {'object_name': 'EmailAddressForPurchaseOrder', '_ormbases': ['crm.EmailAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.PurchaseOrder']"}),
            'emailaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.EmailAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.emailaddressforsalescontract': {
            'Meta': {'object_name': 'EmailAddressForSalesContract', '_ormbases': ['crm.EmailAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.SalesContract']"}),
            'emailaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.EmailAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.invoice': {
            'Meta': {'object_name': 'Invoice', '_ormbases': ['crm.SalesContract']},
            'derivatedFromQuote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Quote']", 'null': 'True', 'blank': 'True'}),
            'payableuntil': ('django.db.models.fields.DateField', [], {}),
            'paymentBankReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'salescontract_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.SalesContract']", 'unique': 'True', 'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.phoneaddress': {
            'Meta': {'object_name': 'PhoneAddress'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'crm.phoneaddressforcontact': {
            'Meta': {'object_name': 'PhoneAddressForContact', '_ormbases': ['crm.PhoneAddress']},
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'phoneaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PhoneAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.phoneaddressforcontract': {
            'Meta': {'object_name': 'PhoneAddressForContract', '_ormbases': ['crm.PhoneAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contract']"}),
            'phoneaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PhoneAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.phoneaddressforpurchaseorder': {
            'Meta': {'object_name': 'PhoneAddressForPurchaseOrder', '_ormbases': ['crm.PhoneAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.PurchaseOrder']"}),
            'phoneaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PhoneAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.phoneaddressforsalescontract': {
            'Meta': {'object_name': 'PhoneAddressForSalesContract', '_ormbases': ['crm.PhoneAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.SalesContract']"}),
            'phoneaddress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PhoneAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.position': {
            'Meta': {'object_name': 'Position'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'overwriteProductPrice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'positionNumber': ('django.db.models.fields.IntegerField', [], {}),
            'positionPricePerUnit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Product']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'sentOn': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shipmentID': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Supplier']", 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Unit']", 'null': 'True', 'blank': 'True'})
        },
        'crm.postaladdress': {
            'Meta': {'object_name': 'PostalAddress'},
            'addressline1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline4': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'prename': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'crm.postaladdressforcontact': {
            'Meta': {'object_name': 'PostalAddressForContact', '_ormbases': ['crm.PostalAddress']},
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'postaladdress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PostalAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.postaladdressforcontract': {
            'Meta': {'object_name': 'PostalAddressForContract', '_ormbases': ['crm.PostalAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contract']"}),
            'postaladdress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PostalAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.postaladdressforpurchaseorder': {
            'Meta': {'object_name': 'PostalAddressForPurchaseOrder', '_ormbases': ['crm.PostalAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.PurchaseOrder']"}),
            'postaladdress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PostalAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.postaladdressforsalescontract': {
            'Meta': {'object_name': 'PostalAddressForSalesContract', '_ormbases': ['crm.PostalAddress']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.SalesContract']"}),
            'postaladdress_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.PostalAddress']", 'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'crm.price': {
            'Meta': {'object_name': 'Price'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Currency']"}),
            'customerGroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.CustomerGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Product']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Unit']"}),
            'validfrom': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'validuntil': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'crm.product': {
            'Meta': {'object_name': 'Product'},
            'accoutingProductCategorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounting.ProductCategorie']", 'null': 'True', 'blank': "'True'"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'defaultunit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Unit']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': "'True'"}),
            'productNumber': ('django.db.models.fields.IntegerField', [], {}),
            'tax': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Tax']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'crm.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contract']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Currency']"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'externalReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_polstmodified'", 'to': "orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relpostaff'", 'null': 'True', 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Supplier']"})
        },
        'crm.purchaseorderposition': {
            'Meta': {'object_name': 'PurchaseOrderPosition', '_ormbases': ['crm.Position']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.PurchaseOrder']"}),
            'position_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.Position']", 'unique': 'True', 'primary_key': 'True'})
        },
        'crm.quote': {
            'Meta': {'object_name': 'Quote', '_ormbases': ['crm.SalesContract']},
            'salescontract_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.SalesContract']", 'unique': 'True', 'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'validuntil': ('django.db.models.fields.DateField', [], {})
        },
        'crm.salescontract': {
            'Meta': {'object_name': 'SalesContract'},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contract']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Currency']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Customer']"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'externalReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'True'", 'related_name': "'db_lstscmodified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relscstaff'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'crm.salescontractposition': {
            'Meta': {'object_name': 'SalesContractPosition', '_ormbases': ['crm.Position']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.SalesContract']"}),
            'position_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.Position']", 'unique': 'True', 'primary_key': 'True'})
        },
        'crm.supplier': {
            'Meta': {'object_name': 'Supplier', '_ormbases': ['crm.Contact']},
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'offersShipmentToCustomers': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'crm.tax': {
            'Meta': {'object_name': 'Tax'},
            'accountActiva': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relaccountactiva'", 'null': 'True', 'to': "orm['accounting.Account']"}),
            'accountPassiva': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relaccountpassiva'", 'null': 'True', 'to': "orm['accounting.Account']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxrate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'crm.unit': {
            'Meta': {'object_name': 'Unit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fractionFactorToNextHigherUnit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isAFractionOf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Unit']", 'null': 'True', 'blank': 'True'}),
            'shortName': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'crm.unittransform': {
            'Meta': {'object_name': 'UnitTransform'},
            'factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fromUnit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromfromunit'", 'to': "orm['crm.Unit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Product']"}),
            'toUnit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromtounit'", 'to': "orm['crm.Unit']"})
        }
    }

    complete_apps = ['crm']