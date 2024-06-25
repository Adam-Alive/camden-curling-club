# Testing

> Return to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all HTML files.

| Template | Result| Screenshot | Notes |
| --- | --- | --- | --- |
| index (public) | Pass | ![screenshot](documentation/validation/html/index-public.png) | Errors due to extension of base.html. |
| index (logged-in) | Pass | ![screenshot](documentation/validation/html/index-logged-in.png) | Errors due to extension of base html. |
| booking_list | Pass | ![screenshot](documentation/validation/html/booking-list.png) | | Errors due to extension of base.html.|
| edit_bookings|  Pass| ![screenshot](documentation/validation/html/edit-bookings.png) | Errors due to extension of base.html. |
| my_bookings | Pass | ![screenshot](documentation/validation/html/my-bookings.png) | Errors due to extension of base.html. |
| faq_list | Pass | ![screenshot](documentation/validation/html/faqs.png) | Errors due to extension of base.html.|
| edit_caption | Pass | ![screenshot](documentation/validation/html/edit-caption.png) |Errors due to extension of base.html. |
| galleryimage_list | Pass | ![screenshot](documentation/validation/html/gallery-image-list.png) | |Errors due to extension of base.html.|
| my_pictures | Pass | ![screenshot](documentation/validation/html/my-pictures.png) | Errors due to extension of base.html.|
| network_list |  | ![screenshot](documentation/validation/html/network.png) | Errors due to extension of base.html. |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate the CSS file.

- Result: Pass, no errors:

 ![screenshot](documentation/validation/css.png) 

### JavaScript

I have not undertaken any JS validation since the only scripts used in the base.html are imported from reliable sources ie. Bootstrap and Font Awesome.

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files.

| File | Screenshot | Notes |
| --- |--- | --- |
| settings.py |![screenshot](documentation/validation/py/settings.png) | No errors |
| bookings/models.py |![screenshot](documentation/validation/py/bookings-models.png) | L28, E122 continuation line missing indentation or outdented. This was corrected.|
| bookings/test_forms.py |![screenshot](documentation/validation/py/bookings-test-forms.png) | no errors |
| bookings/testviews.py |![screenshot](documentation/validation/py/bookings-test-views.png) |no errors |
| bookings/urls.py |![screenshot](documentation/validation/py/bookings-urls.png) |no errors |
| bookings/views.py |![screenshot](documentation/validation/py/bookings-views.png) | no errors|
| faqs/test_views.py |![screenshot](documentation/validation/py/test-views.png) | no errors|
| faqs/urls.py |![screenshot](documentation/validation/py/faqs-urls.png) | no errors|
| faqs/views.py |![screenshot](documentation/validation/py/faqs-views.png) | no errors|
| faqs/models.py |![screenshot](documentation/validation/py/models.png) |no errors |
| gallery/forms.py |![screenshot](documentation/validation/py/gallery-forms.png) | no errors|
| gallery/models.py |![screenshot](documentation/validation/py/gallery-models.png) |no errrors |
| galery/test_forms.py |![screenshot](documentation/validation/py/gallery-test-forms.png) |no errors |
| gallery/urls.py |![screenshot](documentation/validation/py/gallery-urls.png) | no errors|
| gallery/views.py |![screenshot](documentation/validation/py/gallery-views.png) | no errors|
| home/test_views.py |![screenshot](documentation/validation/py/home-test-views.png) | no errors|
| home/urls.py |![screenshot](documentation/validation/py/home-urls.png) |no errors |
| home/views.py |![screenshot](documentation/validation/py/home-views.png) |no errors |
| network/models.py |![screenshot](documentation/validation/py/network-models.png) | no errors|
| network/test_views.py |![screenshot](documentation/validation/py/network-test-views.png) | Tno errors|
| network/urls.py |![screenshot](documentation/validation/py/network-urls.png) |no errors |
| network/views.py |![screenshot](documentation/validation/py/network-views.png) | no errors|

## Browser Compatibility
I've tested my deployed project on Chrome, Edge and Safari to check for compatibility issues.

I tested each browser on the homepage, and then logged in to view each feature. I have provided a summary of these tests below with a screenshot of the homepage or gallery.

| Browser | Home/Gallery | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/screens/chrome.png) | Works as expected |
| Edge | ![screenshot](documentation/screens/edge.png) | Works as expected |
| Safari | ![screenshot](documentation/screens/safari.png) | Works as expected |

## Responsiveness

I deployed the project early on and tested on three of my own devices throughout the development process:

- Moto (g8) power
- HP Desktop (24")
- MacBook Air (13")

I also used Dev Tools to test on a tablet device.

I tested the responsiveness of the homepage and each stage of the game and have provided a summary of these tests below with a screenshot of the home or faqs page.

| Device | Home/Gallery/Faqs | Notes |
| --- | --- | --- |
| Moto(g8) mobile (own) | ![screenshot](documentation/screens/phone.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/screens/tablet.png) | Works as expected |
| MacBook Air (own) | ![screenshot](documentation/screens/apple.jpg) | Works as expected |
| HP Desktop (own) | ![screenshot](documentation/screens/hp.jpg) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

All pages, on both mobile and desktop, achieved 100%

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/screens/m-home.png) | ![screenshot](documentation/screens/d-home.png) |
| Bookings | ![screenshot](documentation/screens/m-bookings.png) | ![screenshot](documentation/screens/d-bookings.png) | |
| FAQS | ![screenshot](documentation/screens/m-faqs.png) | ![screenshot](documentation/screens/d-faqs.png) |
| Gallery| ![screenshot](documentation/screens/m-gallery.png) | ![screenshot](documentation/screens/d-gallery.png) |
| Network| ![screenshot](documentation/screens/m-network.png) | ![screenshot](documentation/screens/d-network.png) |
| Logout | ![screenshot](documentation/screens/m-logout.png) | ![screenshot](documentation/screens/d-logout.png) |

## Defensive Programming

Defensive programming (defensive design) is extremely important!

Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses


MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

**Defensive programming has been manually tested and the Pass/Fail outcomes summarised below.**

| Page | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Click on Logo | Redirection to Home page | Pass |TEST |TEST |
| | Click on Home link in navbar | Redirection to Home page | Pass | | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| Gallery | | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | | |
| | Load gallery images | All images load as expected | Pass | |
| repeat for all remaining pages | x | x | x | x | x |

## User Story Testing

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

| User Story | Screenshot |
| --- | --- |
| As a new user, I would like to land on an informative and engaging home page so that I can learn about the club.| ![screenshot](documentation/features/home-non-member.png) |
|  As a new user, I would like to submit my contact details so that I can register my membership. | ![screenshot](documentation/features/register.png) |
|  As a member, I would like to enter my login details so that I can access the members' area. | ![screenshot](documentation/features/login.png) |
|  As a member, I would like to logout so that I can know my session has been closed securely. | ![screenshot](documentation/features/logout-1.png) ![screenshot](documentation/features/logout-2.png) |
|  As a member, I would like to submit a question for display on the FAQs page.| A 'could have' not completed during this iteration. |
|  As a member, I would like to book a practice session so that I can attend at a time that suits me. | ![screenshot](documentation/features/bookings.png) |
|  As a member, I would like to amend or cancel a practice session so that I can change my plans. | ![screenshot](documentation/features/bookings-my-bookings.png) |
| As a member, I would like to know if the booking time I want is available so that I can make another choice if necessary. | A 'could have' not completed during this iteration.|
|  As a member, I would like to add images to the gallery so that I can share my curling experiences with other members. | ![screenshot](documentation/features/gallery-upload.png)  ![screenshot](documentation/features/gallery-my-pictures.png) |
| As a site administrator, I would like to access the administrator panel so that I can manage the club membership and site's pages. | ![screenshot](documentation/features/admin-1.png) ![screenshot](documentation/features/admin-2.png)  |
|  As a site administrator, I would like to know when a new member has registered so that I can email them about their membership options. | A 'won't have' not completed during this iteration. |
|  As a site administrator, I would like to manage content on the FAQs page so that I can provide information to members.| ![screenshot](documentation/features/faqs-1.png) ![screenshot](documentation/features/faqs-2.png) ![screenshot](documentation/features/faqs-3.png)|
|  As a site administrator, I would like to approve or delete images added to the gallery so that I can filter out any objectionable material.| ![screenshot](documentation/features/admin-gall-1.png) ![screenshot](documentation/features/admin-gall-2.png)|
|  As a site administrator, I would like to manage content on the curling network page so that I can keep members informed of other curling venues. | ![screenshot](documentation/features/admin-net-1.png)  ![screenshot](documentation/features/admin-net-2.png)|

## Automated Testing

I have conducted a series of automated tests on my application and fully acknowledge that, in a real-world scenario, an extensive set of additional tests would be required

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then conducted the following:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

## Bugs

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/Adam-Alive/camden-curling-club/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AAdam-Alive%2Fcamden-curling-club%20label%3Abug&label=bugs)](https://github.com/Adam-Alive/camden-curling-club/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/Adam-Alive/camden-curling-club/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/Adam-Alive/camden-curling-club/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/Adam-Alive/camden-curling-club/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/Adam-Alive/camden-curling-club/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/Adam-Alive/camden-curling-club)](https://github.com/Adam-Alive/camden-curling-club/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/Adam-Alive/camden-curling-club)](https://github.com/Adam-Alive/camden-curling-club/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/Adam-Alive/camden-curling-club/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/Adam-Alive/camden-curling-club/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/Adam-Alive/camden-curling-club/issues/5) | Open |

## Unfixed Bugs

Some examples:

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

> There are no remaining bugs that I am aware of.
