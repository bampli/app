# swagger_client.FacilityApi

All URIs are relative to *https://virtserver.swaggerhub.com/motta/bampli/1.0.0-oas3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_facility**](FacilityApi.md#add_facility) | **POST** /facility/ | Create a new Facility
[**add_wip**](FacilityApi.md#add_wip) | **POST** /wip/ | Create a new Wip
[**delete_facility**](FacilityApi.md#delete_facility) | **DELETE** /facility/{facilityid} | Delete a Facility
[**delete_wip**](FacilityApi.md#delete_wip) | **DELETE** /wip/{wipid} | Delete a Wip
[**get_facility**](FacilityApi.md#get_facility) | **GET** /facility/{facilityid} | Load an individual Facility
[**get_wip**](FacilityApi.md#get_wip) | **GET** /wip/{wipid} | Load an individual Wip
[**search_facility**](FacilityApi.md#search_facility) | **GET** /facility/ | Load the list of Facilities
[**search_wips**](FacilityApi.md#search_wips) | **GET** /wip/ | Load the list of Wips
[**update_facility**](FacilityApi.md#update_facility) | **PUT** /facility/{facilityid} | Update a Facility
[**update_wip**](FacilityApi.md#update_wip) | **PUT** /wip/{wipid} | Update a Wip

# **add_facility**
> Facility add_facility(body)

Create a new Facility

Adds a Facility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Facility() # Facility | 

try:
    # Create a new Facility
    api_response = api_instance.add_facility(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->add_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Facility**](Facility.md)|  | 

### Return type

[**Facility**](Facility.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_wip**
> Wip add_wip(body)

Create a new Wip

Adds a Wip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Wip() # Wip | 

try:
    # Create a new Wip
    api_response = api_instance.add_wip(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->add_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Wip**](Wip.md)|  | 

### Return type

[**Wip**](Wip.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_facility**
> delete_facility(facilityid)

Delete a Facility

Deletes a Facility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
facilityid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Facility

try:
    # Delete a Facility
    api_instance.delete_facility(facilityid)
except ApiException as e:
    print("Exception when calling FacilityApi->delete_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facilityid** | **str**| Identifier of the Facility | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wip**
> delete_wip(wipid)

Delete a Wip

Deletes a Wip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
wipid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Wip

try:
    # Delete a Wip
    api_instance.delete_wip(wipid)
except ApiException as e:
    print("Exception when calling FacilityApi->delete_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wipid** | **str**| Identifier of the Wip | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility**
> Facility get_facility(facilityid)

Load an individual Facility

Loads a Facility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
facilityid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Facility

try:
    # Load an individual Facility
    api_response = api_instance.get_facility(facilityid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facilityid** | **str**| Identifier of the Facility | 

### Return type

[**Facility**](Facility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wip**
> Wip get_wip(wipid)

Load an individual Wip

Loads a Wip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
wipid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Wip

try:
    # Load an individual Wip
    api_response = api_instance.get_wip(wipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wipid** | **str**| Identifier of the Wip | 

### Return type

[**Wip**](Wip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_facility**
> list[Facility] search_facility(size=size, page=page, sort=sort, name=name, company_id=company_id)

Load the list of Facilities

Loads list of Facilities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by name (optional)
company_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by company_id (optional)

try:
    # Load the list of Facilities
    api_response = api_instance.search_facility(size=size, page=page, sort=sort, name=name, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->search_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC | [optional] 
 **name** | **str**| Allows to filter the collections of result by name | [optional] 
 **company_id** | **str**| Allows to filter the collections of result by company_id | [optional] 

### Return type

[**list[Facility]**](Facility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_wips**
> list[Wip] search_wips(size=size, page=page, sort=sort, name=name, facility_id=facility_id)

Load the list of Wips

Loads list of Wips

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by name (optional)
facility_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by facility_id (optional)

try:
    # Load the list of Wips
    api_response = api_instance.search_wips(size=size, page=page, sort=sort, name=name, facility_id=facility_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->search_wips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC | [optional] 
 **name** | **str**| Allows to filter the collections of result by name | [optional] 
 **facility_id** | **str**| Allows to filter the collections of result by facility_id | [optional] 

### Return type

[**list[Wip]**](Wip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_facility**
> Facility update_facility(body, facilityid)

Update a Facility

Stores a Facility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Facility() # Facility | 
facilityid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Facility

try:
    # Update a Facility
    api_response = api_instance.update_facility(body, facilityid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->update_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Facility**](Facility.md)|  | 
 **facilityid** | **str**| Identifier of the Facility | 

### Return type

[**Facility**](Facility.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wip**
> Wip update_wip(body, wipid)

Update a Wip

Stores a Wip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTP_BASIC
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Wip() # Wip | 
wipid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Wip

try:
    # Update a Wip
    api_response = api_instance.update_wip(body, wipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->update_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Wip**](Wip.md)|  | 
 **wipid** | **str**| Identifier of the Wip | 

### Return type

[**Wip**](Wip.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

