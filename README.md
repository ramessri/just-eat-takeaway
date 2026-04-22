# just-eat-takeaway

This repo is my submission for the Just Eat Takeaway Early Career SWE role.


Steps:

1. Testing the API with multiple postcodes, learnt that Just Eat blocked me because I didn't send a User-Agent, so they returned an empty body or an HTML error page, and .json() choked trying to parse it. (403 error)

2. Built the app with Forms -> Views -> Services

3. Error Handling: I am seeing 4 types:
Invalid postcode format (e.g. ZZZ, 123, empty after stripping) — caught at the form level
API returns non-200 (bad postcode that's format-valid but doesn't exist, API down, rate limited) — caught at the service level
API times out / network error — caught at the service level
API returns 200 but empty restaurant list — caught at the view/template level