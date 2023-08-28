<p><h1>Unittests and Integration Tests</h1> :fire: </p>

<p><h2>Description</h2> :house: </p>
In this project, I began to learn more about `Unittest` and `Integration` Tests.
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.
<br>
The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?
<br>
Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.
<br>
Integration tests will test interactions between every part of your code.
<br>
Execute your tests with

## Tasks :pencil:
| Task | Description |
|------|-------------|
|[0. Parameterize a unit test](./test_utils.py) | Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.|
| [1. Parameterize a unit test](./test_utils.py) | Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand)
| [2. Mock HTTP calls](./test_utils.py) | Familiarize yourself with the utils.get_json function.<br>Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.|
| [3. Parameterize and patch](./test_utils.py) | Read about memoization and familiarize yourself with the utils.memoize decorator.<br>Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.<br>Inside test_memoize, define following class
| [4. Parameterize and patch as decorators](./test_client.py) | Familiarize yourself with the client.GithubOrgClient class.<br>In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.<br>This method should test that GithubOrgClient.org returns the correct value.<br>Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.|
| [5. Mocking a property](./test_client.py) | memoize turns methods into properties. Read up on how to mock a property (see resource).<br>Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.<br>Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.<br>Test that the result of _public_repos_url is the expected one based on the mocked payload.|
| [6. More patching](./test_client.py) | Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.<br>Use @patch as a decorator to mock get_json and make it return a payload of your choice.<br>Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.<br>Test that the list of repos is what you expect from the chosen payload.<br><br>Test that the mocked property and the mocked get_json was called once.|
| [7. Parameterize](./test_client.py) | Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.<br>Parametrize the test with the following inputs
|[8. Integration test: fixtures](./test_client.py) | We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.<br>Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.|
| [9. Integration tests](./test_client.py) | Implement the test_public_repos method to test GithubOrgClient.public_repos.<br>Make sure that the method returns the expected results based on the fixtures.<br>Implement test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and make sure the result matches the expected value from the fixtures.|

## Author
[Betini Akarandut](www.github.com/betiniakarandut)
