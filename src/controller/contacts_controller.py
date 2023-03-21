from hubspot.crm.contacts import ApiException
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
import logging


class ContactsController():

    @classmethod
    def conection_api(self, token):
        api_client = HubSpot(access_token=token)
        return api_client

    @classmethod
    def test_contacts(self, token):
        logger = logging.getLogger(__name__)
        try:
            # Conection Hubspot
            api = self.conection_api(token)

            # Get 100 contacts
            contacts_api = api.crm.contacts
            all_contacts = contacts_api.basic_api.get_page(
                limit=2,
                properties=["phone"],
                archived=False)
            # Convert contacts_object to dict
            dict_all_contacts = all_contacts.to_dict()

            # IF 'phone'==None, so update 'phone'=660049971
            for contact in dict_all_contacts['results']:
                if contact['properties']['phone'] is None:
                    contact['properties']['phone'] = 660049971
                    simple_public_object_input = SimplePublicObjectInput(
                        properties=contact['properties'])
                    api_response = contacts_api.basic_api.update(
                        contact_id=contact['id'],
                        simple_public_object_input=simple_public_object_input)

        except ApiException as e:
            logger.error("Exception when calling basic_api: %s\n" % e)
        except Exception as e:
            logger.error("Exception when calling test_contacts: %s\n" % e)
