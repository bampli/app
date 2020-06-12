# swagger_client.FacilityApi

All URIs are relative to *https://virtserver.swaggerhub.com/motta/bampli/1.0.0-oas3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_facility**](FacilityApi.md#add_facility) | **POST** /facility | Add Facility
[**add_wip**](FacilityApi.md#add_wip) | **POST** /wip | Add Wip
[**get_facility**](FacilityApi.md#get_facility) | **GET** /facility | Get Facility
[**search_wip**](FacilityApi.md#search_wip) | **GET** /wip | Get Wip

# **add_facility**
> add_facility(body=body)

Add Facility

Adds a Facility to the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
body = swagger_client.Facility() # Facility | Facility item to add (optional)

try:
    # Add Facility
    api_instance.add_facility(body=body)
except ApiException as e:
    print("Exception when calling FacilityApi->add_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Facility**](Facility.md)| Facility item to add | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_wip**
> add_wip(body=body)

Add Wip

Adds a Wip to the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
body = swagger_client.Wip() # Wip | Wip item to add (optional)

try:
    # Add Wip
    api_instance.add_wip(body=body)
except ApiException as e:
    print("Exception when calling FacilityApi->add_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Wip**](Wip.md)| Wip item to add | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facility**
> list[Facility] get_facility(search_string=search_string, skip=skip, limit=limit)

Get Facility

Search for an available Facility in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
search_string = 'search_string_example' # str | pass an optional search string for looking up inventory (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # Get Facility
    api_response = api_instance.get_facility(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->get_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for looking up inventory | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[Facility]**](Facility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_wip**
> list[Wip] search_wip(search_string=search_string, skip=skip, limit=limit)

Get Wip

Search for an available Wip in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FacilityApi()
search_string = 'search_string_example' # str | pass an optional search string for looking up wip (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # Get Wip
    api_response = api_instance.search_wip(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->search_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for looking up wip | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[Wip]**](Wip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

