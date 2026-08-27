"""Minimal M0 smoke tests."""


def test_project_imports() -> None:
    import api.main

    assert api.main.create_app() is None
