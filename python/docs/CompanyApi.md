# swagger_client.CompanyApi

All URIs are relative to *https://virtserver.swaggerhub.com/motta/bampli/1.0.0-oas3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company**](CompanyApi.md#add_company) | **POST** /company/ | Create a new Company
[**add_product**](CompanyApi.md#add_product) | **POST** /product/ | Create a new Product
[**delete_company**](CompanyApi.md#delete_company) | **DELETE** /company/{companyid} | Delete a Company
[**delete_product**](CompanyApi.md#delete_product) | **DELETE** /product/{productid} | Delete a Product
[**get_company**](CompanyApi.md#get_company) | **GET** /company/{companyid} | Load an individual Company
[**get_product**](CompanyApi.md#get_product) | **GET** /product/{productid} | Load an individual Product
[**search_companies**](CompanyApi.md#search_companies) | **GET** /company/ | Load the list of Companies
[**search_products**](CompanyApi.md#search_products) | **GET** /product/ | Load the list of Products
[**update_company**](CompanyApi.md#update_company) | **PUT** /company/{companyid} | Update a Company
[**update_product**](CompanyApi.md#update_product) | **PUT** /product/{productid} | Update a Product

# **add_company**
> Company add_company(body)

Create a new Company

Adds a Company

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Company() # Company | 

try:
    # Create a new Company
    api_response = api_instance.add_company(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->add_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Company**](Company.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product**
> Product add_product(body)

Create a new Product

Adds a Product

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Product() # Product | 

try:
    # Create a new Product
    api_response = api_instance.add_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company**
> delete_company(companyid)

Delete a Company

Deletes a Company

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
companyid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Company

try:
    # Delete a Company
    api_instance.delete_company(companyid)
except ApiException as e:
    print("Exception when calling CompanyApi->delete_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyid** | **str**| Identifier of the Company | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> delete_product(productid)

Delete a Product

Deletes a Product

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
productid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Product

try:
    # Delete a Product
    api_instance.delete_product(productid)
except ApiException as e:
    print("Exception when calling CompanyApi->delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **str**| Identifier of the Product | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> Company get_company(companyid)

Load an individual Company

Loads a Company

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyApi()
companyid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Company

try:
    # Load an individual Company
    api_response = api_instance.get_company(companyid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyid** | **str**| Identifier of the Company | 

### Return type

[**Company**](Company.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(productid)

Load an individual Product

Loads a Product

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyApi()
productid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Product

try:
    # Load an individual Product
    api_response = api_instance.get_product(productid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **str**| Identifier of the Product | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_companies**
> list[Company] search_companies(size=size, page=page, sort=sort, name=name)

Load the list of Companies

Loads list of Companies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by the value of name (optional)

try:
    # Load the list of Companies
    api_response = api_instance.search_companies(size=size, page=page, sort=sort, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->search_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC | [optional] 
 **name** | **str**| Allows to filter the collections of result by the value of name | [optional] 

### Return type

[**list[Company]**](Company.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_products**
> list[Product] search_products(size=size, page=page, sort=sort, name=name, company_id=company_id)

Load the list of Products

Loads list of Products

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by name (optional)
company_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by company_id (optional)

try:
    # Load the list of Products
    api_response = api_instance.search_products(size=size, page=page, sort=sort, name=name, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->search_products: %s\n" % e)
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

[**list[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company**
> Company update_company(body, companyid)

Update a Company

Stores a Company

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Company() # Company | 
companyid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Company

try:
    # Update a Company
    api_response = api_instance.update_company(body, companyid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->update_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Company**](Company.md)|  | 
 **companyid** | **str**| Identifier of the Company | 

### Return type

[**Company**](Company.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> Product update_product(body, productid)

Update a Product

Stores a Product

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Product() # Product | 
productid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Product

try:
    # Update a Product
    api_response = api_instance.update_product(body, productid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 
 **productid** | **str**| Identifier of the Product | 

### Return type

[**Product**](Product.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

