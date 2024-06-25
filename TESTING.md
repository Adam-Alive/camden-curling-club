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
| bookings/models.py |![screenshot](documentation/validation/py/bookings-models.png) | L28, E122 continuation line missing indentation or outdented.|
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
| gallery/urls.py |![screenshot](documentation/validation/py/.png) | TBC|
| gallery/views.py |![screenshot](documentation/validation/py/.png) | TBC|
| home/test_views.py |![screenshot](documentation/validation/py/home-test-views.png) | no errors|
| home/urls.py |![screenshot](documentation/validation/py/home-urls.png) |no errors |
| home/views.py |![screenshot](documentation/validation/py/home-views.png) |no errors |
| network/models.py |![screenshot](documentation/validation/py/.png) | TBC|
| network/test_views.py |![screenshot](documentation/validation/py/.png) | TBC|
| network/urls.py |![screenshot](documentation/validation/py/network-urls.png) |no errors |
| network/views.py |![screenshot](documentation/validation/py/network-views.png) | no errors|





| x | x | x | repeat for all remaining Python files |


`# noqa` = **NO Quality Assurance**

**NOTE**: You must include 2 *spaces* before the `#`, and 1 *space* after the `#`.

Do not use `# noqa` all over your project just to clear down validation errors!
This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes strings or variables get too long, or long `if` conditional statements.
These are acceptable instances to use the `# noqa`.

When trying to fix "line too long" errors, try to avoid using `/` to split lines.
A better approach would be to use any type of opening bracket, and hit Enter just after that.

Any opening bracket type will work: `(`, `[`, `{`.

By using an opening bracket, Python knows where to appropriately indent the next line of code,
without having to "guess" yourself and attempt to tab to the correct indentation level.



## Browser Compatibility

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Sample browser testing documentation:

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |

| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-about.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-etc.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/responsive-xl-home.png) | ![screenshot](documentation/responsiveness/responsive-xl-about.png) | ![screenshot](documentation/responsiveness/responsive-xl-contact.png) | ![screenshot](documentation/responsiveness/responsive-xl-etc.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsiveness/responsive-4k-home.png) | ![screenshot](documentation/responsiveness/responsive-4k-about.png) | ![screenshot](documentation/responsiveness/responsive-4k-contact.png) | ![screenshot](documentation/responsiveness/responsive-4k-etc.png) | Noticeable scaling issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsiveness/responsive-pixel-home.png) | ![screenshot](documentation/responsiveness/responsive-pixel-about.png) | ![screenshot](documentation/responsiveness/responsive-pixel-contact.png) | ![screenshot](documentation/responsiveness/responsive-pixel-etc.png) | Works as expected |
| iPhone 14 | ![screenshot](documentation/responsiveness/responsive-iphone-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-etc.png) | Works as expected |
| repeat for any other tested browsers | x | x | x | x | x |

## Lighthouse Audit

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

Defensive programming (defensive design) is extremely important!

Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

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
| As a new user, I would like to land on an informative and engaging home page so that I can learn about the club.| ![screenshot](documentation/features/feature01.png) |
|  As a new user, I would like to submit my contact details so that I can register my membership. | ![screenshot](documentation/features/feature02.png) |
|  As a member, I would like to enter my login details so that I can access the members' area. | ![screenshot](documentation/features/feature03.png) |
|  As a member, I would like to logout so that I can know my session has been closed securely. | ![screenshot](documentation/features/feature04.png) |
|  As a member, I would like to submit a question for display on the FAQs page.| ![screenshot](documentation/features/feature05.png) |
|  As a member, I would like to book a practice session so that I can attend at a time that suits me. | ![screenshot](documentation/features/feature06.png) |
|  As a member, I would like to amend or cancel a practice session so that I can change my plans. | ![screenshot](documentation/features/feature07.png) |
| As a member, I would like to know if the booking time I want is available so that I can make another choice if necessary. | ![screenshot](documentation/features/feature08.png) |
|  As a member, I would like to add images to the gallery so that I can share my curling experiences with other members. | ![screenshot](documentation/features/feature09.png) |
| As a site administrator, I would like to access the administrator panel so that I can manage the club membership and site's pages. | ![screenshot](documentation/features/feature09.png) |
|  As a site administrator, I would like to know when a new member has registered so that I can email them about their membership options. | ![screenshot](documentation/features/feature09.png) |
|  As a site administrator, I would like to manage content on the FAQs page so that I can provide information to members.| ![screenshot](documentation/features/feature09.png) |
|  As a site administrator, I would like to approve or delete images added to the gallery so that I can filter out any objectionable material.| ![screenshot](documentation/features/feature09.png) |
|  As a site administrator, I would like to manage content on the curling network page so that I can keep members informed of other curling venues. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

Adjust the code below (file names, etc.) to match your own project files/folders.

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

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

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

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

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

> There are no remaining bugs that I am aware of.
