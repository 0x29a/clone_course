clone_course
#############################

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

Django application that provides a service for cloning courses in an Open edX instance.

The application provides a RESTful API that can be used to create a new course by cloning an existing one.
The application uses Celery to perform the cloning operation in the background,
and provides a task status endpoint to check the status of the task.


Getting Started
***************

Prerequisites
==========
- Docker and Docker Compose
- Python 3.x
- Virtualenv

Devstack Setup
==========
1. Ensure that the Open edX platform devstack is running. Devstack won't run the Celery message broker by default.
   Ensure to start the redis broker by running the command ``make dev.up.redis``.
   (note: edx-platform should have the changes from `this commit`_)
.. _this commit: https://github.com/open-craft/edx-platform/commit/6dbef5a2478cc683bc17111024892edabf47b50e
2. Create a Python 3 virtual environment for the project.
3. Install the required Python packages by running the command:``make dev.requirements``.
4. Start the services for this project by running the command:``make dev.up``.
5. Setup required oauth application with LMS, by running the command:``./provision-clone_course.sh``.

Deploying
=========

TODO: How can a new user go about deploying this component? Is it just a few
commands? Is there a larger how-to that should be linked here?

PLACEHOLDER: For details on how to deploy this component, see the `deployment how-to`_

.. _deployment how-to: https://docs.openedx.org/projects/clone_course/how-tos/how-to-deploy-this-component.html

Usage
-----

API Endpoints
*************

**Clone course**

``POST /api/v1/clone/clone/``

This API endpoint is used to clone an existing course to a new course.

The request body should contain a JSON object with the following fields:

- ``source_course_id``: The ID of the course to clone.
- ``destination_course_id``: The ID of the new course.

Example Request:

.. code-block:: json

    {
        "source_course_id": "course-v1:edX+DemoX+Demo_Course",
        "destination_course_id": "course-v1:new+TestX+Demo_Course_Clone",
    }

Example Response:

.. code-block:: json

    {
        "task_id": "4f95e48a-8b68-45dc-942f-9ac19d5af352"
    }

**Check clone status**

``GET /api/v1/clone/status/``

This API endpoint is used to check the status of a cloning task.

The request should include a query parameter ``task_id`` with the ID of the cloning task.

Example Request:

.. code-block:: http

    GET /api/v1/clone/status/?task_id=4f95e48a-8b68-45dc-942f-9ac19d5af352

Example Response:

.. code-block:: json

    {
        "status": "SUCCESS"
    }


Getting Help
************

Documentation
=============

PLACEHOLDER: Start by going through `the documentation`_.  If you need more help see below.

.. _the documentation: https://docs.openedx.org/projects/clone_course

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

More Help
=========

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the
community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide.

https://github.com/openedx/clone_course/issues

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help

License
*******

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to have a discussion about your new feature idea with the maintainers prior to
beginning development to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://open-edx-backstage.herokuapp.com/catalog/default/component/clone_course

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@tcril.org.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/clone_course.svg
    :target: https://pypi.python.org/pypi/clone_course/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/openedx/clone_course/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/openedx/clone_course/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/openedx/clone_course/coverage.svg?branch=main
    :target: https://codecov.io/github/openedx/clone_course?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/clone_course/badge/?version=latest
    :target: https://clone_course.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/clone_course.svg
    :target: https://pypi.python.org/pypi/clone_course/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/openedx/clone_course.svg
    :target: https://github.com/openedx/clone_course/blob/main/LICENSE.txt
    :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
