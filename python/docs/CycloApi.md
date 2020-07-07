# swagger_client.CycloApi

All URIs are relative to *https://virtserver.swaggerhub.com/motta/bampli/1.0.0-oas3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cyclo**](CycloApi.md#add_cyclo) | **POST** /cyclo/ | Create a new Cyclo
[**add_stage**](CycloApi.md#add_stage) | **POST** /stage/ | Create a new Stage
[**add_task**](CycloApi.md#add_task) | **POST** /task/ | Create a new Task
[**delete_cyclo**](CycloApi.md#delete_cyclo) | **DELETE** /cyclo/{cycloid} | Delete a Cyclo
[**delete_stage**](CycloApi.md#delete_stage) | **DELETE** /stage/{stageid} | Delete a Stage
[**delete_task**](CycloApi.md#delete_task) | **DELETE** /task/{taskid} | Delete a Task
[**get_cyclo**](CycloApi.md#get_cyclo) | **GET** /cyclo/{cycloid} | Load an individual Cyclo
[**get_stage**](CycloApi.md#get_stage) | **GET** /stage/{stageid} | Load an individual Stage
[**get_task**](CycloApi.md#get_task) | **GET** /task/{taskid} | Load an individual Task
[**search_cyclos**](CycloApi.md#search_cyclos) | **GET** /cyclo/ | Load the list of Cyclos
[**search_stages**](CycloApi.md#search_stages) | **GET** /stage/ | Load the list of Stages
[**search_tasks**](CycloApi.md#search_tasks) | **GET** /task/ | Load the list of Tasks
[**update_cyclo**](CycloApi.md#update_cyclo) | **PUT** /cyclo/{cycloid} | Update a Cyclo
[**update_stage**](CycloApi.md#update_stage) | **PUT** /stage/{stageid} | Update a Stage
[**update_task**](CycloApi.md#update_task) | **PUT** /task/{taskid} | Update a Task

# **add_cyclo**
> Cyclo add_cyclo(body)

Create a new Cyclo

Adds a Cyclo

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Cyclo() # Cyclo | 

try:
    # Create a new Cyclo
    api_response = api_instance.add_cyclo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->add_cyclo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cyclo**](Cyclo.md)|  | 

### Return type

[**Cyclo**](Cyclo.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_stage**
> Stage add_stage(body)

Create a new Stage

Adds a Stage

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stage() # Stage | 

try:
    # Create a new Stage
    api_response = api_instance.add_stage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->add_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stage**](Stage.md)|  | 

### Return type

[**Stage**](Stage.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task**
> Task add_task(body)

Create a new Task

Adds a Task

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Task() # Task | 

try:
    # Create a new Task
    api_response = api_instance.add_task(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->add_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cyclo**
> delete_cyclo(cycloid)

Delete a Cyclo

Deletes a Cyclo

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
cycloid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Cyclo

try:
    # Delete a Cyclo
    api_instance.delete_cyclo(cycloid)
except ApiException as e:
    print("Exception when calling CycloApi->delete_cyclo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycloid** | **str**| Identifier of the Cyclo | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stage**
> delete_stage(stageid)

Delete a Stage

Deletes a Stage

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
stageid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Stage

try:
    # Delete a Stage
    api_instance.delete_stage(stageid)
except ApiException as e:
    print("Exception when calling CycloApi->delete_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stageid** | **str**| Identifier of the Stage | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(taskid)

Delete a Task

Deletes a Task

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
taskid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Task

try:
    # Delete a Task
    api_instance.delete_task(taskid)
except ApiException as e:
    print("Exception when calling CycloApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskid** | **str**| Identifier of the Task | 

### Return type

void (empty response body)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cyclo**
> Cyclo get_cyclo(cycloid)

Load an individual Cyclo

Loads a Cyclo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
cycloid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Cyclo

try:
    # Load an individual Cyclo
    api_response = api_instance.get_cyclo(cycloid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->get_cyclo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycloid** | **str**| Identifier of the Cyclo | 

### Return type

[**Cyclo**](Cyclo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stage**
> Stage get_stage(stageid)

Load an individual Stage

Loads a Stage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
stageid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Stage

try:
    # Load an individual Stage
    api_response = api_instance.get_stage(stageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->get_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stageid** | **str**| Identifier of the Stage | 

### Return type

[**Stage**](Stage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(taskid)

Load an individual Task

Loads a Task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
taskid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Task

try:
    # Load an individual Task
    api_response = api_instance.get_task(taskid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskid** | **str**| Identifier of the Task | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cyclos**
> list[Cyclo] search_cyclos(size=size, page=page, sort=sort, name=name, company_id=company_id)

Load the list of Cyclos

Loads list of Cyclos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by name (optional)
company_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by company_id (optional)

try:
    # Load the list of Cyclos
    api_response = api_instance.search_cyclos(size=size, page=page, sort=sort, name=name, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->search_cyclos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. | [optional] 
 **name** | **str**| Allows to filter the collections of result by name | [optional] 
 **company_id** | **str**| Allows to filter the collections of result by company_id | [optional] 

### Return type

[**list[Cyclo]**](Cyclo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stages**
> list[Stage] search_stages(size=size, page=page, sort=sort, name=name, cyclo_id=cyclo_id)

Load the list of Stages

Loads list of Stages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC (optional)
name = '\"Painting\"' # str | Allows to filter the collections of result by name (optional)
cyclo_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by cyclo_id (optional)

try:
    # Load the list of Stages
    api_response = api_instance.search_stages(size=size, page=page, sort=sort, name=name, cyclo_id=cyclo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->search_stages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC | [optional] 
 **name** | **str**| Allows to filter the collections of result by name | [optional] 
 **cyclo_id** | **str**| Allows to filter the collections of result by cyclo_id | [optional] 

### Return type

[**list[Stage]**](Stage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks**
> list[Task] search_tasks(size=size, page=page, sort=sort, name=name, stage_id=stage_id)

Load the list of Tasks

Loads list of Tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloApi()
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # float | Number of the page to retrieve. (optional)
sort = '\"name ASC\"' # str | Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC (optional)
name = '\"George Street Brewery\"' # str | Allows to filter the collections of result by name (optional)
stage_id = '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Allows to filter the collections of result by stage_id (optional)

try:
    # Load the list of Tasks
    api_response = api_instance.search_tasks(size=size, page=page, sort=sort, name=name, stage_id=stage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->search_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **float**| Number of the page to retrieve. | [optional] 
 **sort** | **str**| Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC | [optional] 
 **name** | **str**| Allows to filter the collections of result by name | [optional] 
 **stage_id** | **str**| Allows to filter the collections of result by stage_id | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cyclo**
> Cyclo update_cyclo(body, cycloid)

Update a Cyclo

Stores a Cyclo

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Cyclo() # Cyclo | 
cycloid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Cyclo

try:
    # Update a Cyclo
    api_response = api_instance.update_cyclo(body, cycloid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->update_cyclo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cyclo**](Cyclo.md)|  | 
 **cycloid** | **str**| Identifier of the Cyclo | 

### Return type

[**Cyclo**](Cyclo.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stage**
> Stage update_stage(body, stageid)

Update a Stage

Stores a Stage

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stage() # Stage | 
stageid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Stage

try:
    # Update a Stage
    api_response = api_instance.update_stage(body, stageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->update_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stage**](Stage.md)|  | 
 **stageid** | **str**| Identifier of the Stage | 

### Return type

[**Stage**](Stage.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(body, taskid)

Update a Task

Stores a Task

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
api_instance = swagger_client.CycloApi(swagger_client.ApiClient(configuration))
body = swagger_client.Task() # Task | 
taskid = '\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"' # str | Identifier of the Task

try:
    # Update a Task
    api_response = api_instance.update_task(body, taskid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CycloApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Task**](Task.md)|  | 
 **taskid** | **str**| Identifier of the Task | 

### Return type

[**Task**](Task.md)

### Authorization

[HTTP_BASIC](../README.md#HTTP_BASIC)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

