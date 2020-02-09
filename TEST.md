# Implement Test in Python

Can create a one tests.py only, if you create more then 1 file, it will popup message error.

OR

Can create folder and set name tests, and create file __init__.py within folder also.

`tests/__init.py`

## Implement Test Raise Message

You can create an unittest for raise error.

Example:

```python
def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')
```

In this case, we're checking the email, if the value of email are Blank or EmptyString.

So it don't have implement raise message for show to user, this test isn't pass.