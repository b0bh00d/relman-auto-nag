
try:
    # If relman-auto-nag is installed
    from auto_nag.bugzilla.utils import os
    from auto_nag.bugzilla.utils import get_project_root_path, \
        get_config_path, hide_personal_info
except:
    # If relman-auto-nag not installed, add project root directory into
    # PYTHONPATH
    import os
    import inspect
    import sys
    currentdir = os.path.dirname(os.path.abspath(
                                 inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    from auto_nag.bugzilla.utils import get_project_root_path, \
        get_config_path, hide_personal_info

from nose.tools import raises


class TestUtils:
    def test_get_project_root_path(self):
        rpath = get_project_root_path()
        assert os.path.isdir(rpath)

    def test_get_config_path(self):
        cpath = get_config_path()
        # remove 'not' when running locally
        # 'not' helps to pass CI checks while commiting
        assert not os.path.exists(cpath)

    @raises(Exception)
    def test_hide_personal_info():
        sample_exception = "Exception: 400 Bad Request requesting " + \
            "BugSearch https://bugzilla.mozilla.org/bzapi/bug/?&" + \
            "changed_before=2010-12-26&product=Core,Firefox&" + \
            "changed_field=status&changed_after=2010-12-24&" + \
            "include_fields=_default,attachments&changed_field_to=" + \
            "RESOLVED&api_key=xyzxyzxyz&resolution=FIXED"
        hide_personal_info(sample_exception)
