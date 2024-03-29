# coding: utf-8

"""
    Clerk Backend API

    The Clerk REST Backend API, meant to be accessed by backend servers. Please see https://clerk.com/docs for more information.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@clerk.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UsersUserIdBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'primary_email_address_id': 'str',
        'notify_primary_email_address_changed': 'bool',
        'primary_phone_number_id': 'str',
        'primary_web3_wallet_id': 'str',
        'username': 'str',
        'profile_image_id': 'str',
        'password': 'str',
        'password_digest': 'str',
        'password_hasher': 'str',
        'skip_password_checks': 'bool',
        'sign_out_of_other_sessions': 'bool',
        'totp_secret': 'str',
        'backup_codes': 'list[str]',
        'public_metadata': 'object',
        'private_metadata': 'object',
        'unsafe_metadata': 'object',
        'delete_self_enabled': 'bool',
        'create_organization_enabled': 'bool',
        'created_at': 'str'
    }

    attribute_map = {
        'external_id': 'external_id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'primary_email_address_id': 'primary_email_address_id',
        'notify_primary_email_address_changed': 'notify_primary_email_address_changed',
        'primary_phone_number_id': 'primary_phone_number_id',
        'primary_web3_wallet_id': 'primary_web3_wallet_id',
        'username': 'username',
        'profile_image_id': 'profile_image_id',
        'password': 'password',
        'password_digest': 'password_digest',
        'password_hasher': 'password_hasher',
        'skip_password_checks': 'skip_password_checks',
        'sign_out_of_other_sessions': 'sign_out_of_other_sessions',
        'totp_secret': 'totp_secret',
        'backup_codes': 'backup_codes',
        'public_metadata': 'public_metadata',
        'private_metadata': 'private_metadata',
        'unsafe_metadata': 'unsafe_metadata',
        'delete_self_enabled': 'delete_self_enabled',
        'create_organization_enabled': 'create_organization_enabled',
        'created_at': 'created_at'
    }

    def __init__(self, external_id=None, first_name=None, last_name=None, primary_email_address_id=None, notify_primary_email_address_changed=False, primary_phone_number_id=None, primary_web3_wallet_id=None, username=None, profile_image_id=None, password=None, password_digest=None, password_hasher=None, skip_password_checks=None, sign_out_of_other_sessions=None, totp_secret=None, backup_codes=None, public_metadata=None, private_metadata=None, unsafe_metadata=None, delete_self_enabled=None, create_organization_enabled=None, created_at=None):  # noqa: E501
        """UsersUserIdBody - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._first_name = None
        self._last_name = None
        self._primary_email_address_id = None
        self._notify_primary_email_address_changed = None
        self._primary_phone_number_id = None
        self._primary_web3_wallet_id = None
        self._username = None
        self._profile_image_id = None
        self._password = None
        self._password_digest = None
        self._password_hasher = None
        self._skip_password_checks = None
        self._sign_out_of_other_sessions = None
        self._totp_secret = None
        self._backup_codes = None
        self._public_metadata = None
        self._private_metadata = None
        self._unsafe_metadata = None
        self._delete_self_enabled = None
        self._create_organization_enabled = None
        self._created_at = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if primary_email_address_id is not None:
            self.primary_email_address_id = primary_email_address_id
        if notify_primary_email_address_changed is not None:
            self.notify_primary_email_address_changed = notify_primary_email_address_changed
        if primary_phone_number_id is not None:
            self.primary_phone_number_id = primary_phone_number_id
        if primary_web3_wallet_id is not None:
            self.primary_web3_wallet_id = primary_web3_wallet_id
        if username is not None:
            self.username = username
        if profile_image_id is not None:
            self.profile_image_id = profile_image_id
        if password is not None:
            self.password = password
        if password_digest is not None:
            self.password_digest = password_digest
        if password_hasher is not None:
            self.password_hasher = password_hasher
        if skip_password_checks is not None:
            self.skip_password_checks = skip_password_checks
        if sign_out_of_other_sessions is not None:
            self.sign_out_of_other_sessions = sign_out_of_other_sessions
        if totp_secret is not None:
            self.totp_secret = totp_secret
        if backup_codes is not None:
            self.backup_codes = backup_codes
        if public_metadata is not None:
            self.public_metadata = public_metadata
        if private_metadata is not None:
            self.private_metadata = private_metadata
        if unsafe_metadata is not None:
            self.unsafe_metadata = unsafe_metadata
        if delete_self_enabled is not None:
            self.delete_self_enabled = delete_self_enabled
        if create_organization_enabled is not None:
            self.create_organization_enabled = create_organization_enabled
        if created_at is not None:
            self.created_at = created_at

    @property
    def external_id(self):
        """Gets the external_id of this UsersUserIdBody.  # noqa: E501

        The ID of the user as used in your external systems or your previous authentication solution. Must be unique across your instance.  # noqa: E501

        :return: The external_id of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UsersUserIdBody.

        The ID of the user as used in your external systems or your previous authentication solution. Must be unique across your instance.  # noqa: E501

        :param external_id: The external_id of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def first_name(self):
        """Gets the first_name of this UsersUserIdBody.  # noqa: E501

        The first name to assign to the user  # noqa: E501

        :return: The first_name of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UsersUserIdBody.

        The first name to assign to the user  # noqa: E501

        :param first_name: The first_name of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UsersUserIdBody.  # noqa: E501

        The last name to assign to the user  # noqa: E501

        :return: The last_name of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UsersUserIdBody.

        The last name to assign to the user  # noqa: E501

        :param last_name: The last_name of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def primary_email_address_id(self):
        """Gets the primary_email_address_id of this UsersUserIdBody.  # noqa: E501

        The ID of the email address to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :return: The primary_email_address_id of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._primary_email_address_id

    @primary_email_address_id.setter
    def primary_email_address_id(self, primary_email_address_id):
        """Sets the primary_email_address_id of this UsersUserIdBody.

        The ID of the email address to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :param primary_email_address_id: The primary_email_address_id of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._primary_email_address_id = primary_email_address_id

    @property
    def notify_primary_email_address_changed(self):
        """Gets the notify_primary_email_address_changed of this UsersUserIdBody.  # noqa: E501

        If set to `true`, the user will be notified that their primary email address has changed. By default, no notification is sent.  # noqa: E501

        :return: The notify_primary_email_address_changed of this UsersUserIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify_primary_email_address_changed

    @notify_primary_email_address_changed.setter
    def notify_primary_email_address_changed(self, notify_primary_email_address_changed):
        """Sets the notify_primary_email_address_changed of this UsersUserIdBody.

        If set to `true`, the user will be notified that their primary email address has changed. By default, no notification is sent.  # noqa: E501

        :param notify_primary_email_address_changed: The notify_primary_email_address_changed of this UsersUserIdBody.  # noqa: E501
        :type: bool
        """

        self._notify_primary_email_address_changed = notify_primary_email_address_changed

    @property
    def primary_phone_number_id(self):
        """Gets the primary_phone_number_id of this UsersUserIdBody.  # noqa: E501

        The ID of the phone number to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :return: The primary_phone_number_id of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._primary_phone_number_id

    @primary_phone_number_id.setter
    def primary_phone_number_id(self, primary_phone_number_id):
        """Sets the primary_phone_number_id of this UsersUserIdBody.

        The ID of the phone number to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :param primary_phone_number_id: The primary_phone_number_id of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._primary_phone_number_id = primary_phone_number_id

    @property
    def primary_web3_wallet_id(self):
        """Gets the primary_web3_wallet_id of this UsersUserIdBody.  # noqa: E501

        The ID of the web3 wallets to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :return: The primary_web3_wallet_id of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._primary_web3_wallet_id

    @primary_web3_wallet_id.setter
    def primary_web3_wallet_id(self, primary_web3_wallet_id):
        """Sets the primary_web3_wallet_id of this UsersUserIdBody.

        The ID of the web3 wallets to set as primary. It must be verified, and present on the current user.  # noqa: E501

        :param primary_web3_wallet_id: The primary_web3_wallet_id of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._primary_web3_wallet_id = primary_web3_wallet_id

    @property
    def username(self):
        """Gets the username of this UsersUserIdBody.  # noqa: E501

        The username to give to the user. It must be unique across your instance.  # noqa: E501

        :return: The username of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsersUserIdBody.

        The username to give to the user. It must be unique across your instance.  # noqa: E501

        :param username: The username of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def profile_image_id(self):
        """Gets the profile_image_id of this UsersUserIdBody.  # noqa: E501

        The ID of the image to set as the user's profile image  # noqa: E501

        :return: The profile_image_id of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._profile_image_id

    @profile_image_id.setter
    def profile_image_id(self, profile_image_id):
        """Sets the profile_image_id of this UsersUserIdBody.

        The ID of the image to set as the user's profile image  # noqa: E501

        :param profile_image_id: The profile_image_id of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._profile_image_id = profile_image_id

    @property
    def password(self):
        """Gets the password of this UsersUserIdBody.  # noqa: E501

        The plaintext password to give the user. Must be at least 8 characters long, and can not be in any list of hacked passwords.  # noqa: E501

        :return: The password of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsersUserIdBody.

        The plaintext password to give the user. Must be at least 8 characters long, and can not be in any list of hacked passwords.  # noqa: E501

        :param password: The password of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_digest(self):
        """Gets the password_digest of this UsersUserIdBody.  # noqa: E501

        In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The digests should be generated with one of the supported algorithms. The hashing algorithm can be specified using the `password_hasher` property.  # noqa: E501

        :return: The password_digest of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._password_digest

    @password_digest.setter
    def password_digest(self, password_digest):
        """Sets the password_digest of this UsersUserIdBody.

        In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The digests should be generated with one of the supported algorithms. The hashing algorithm can be specified using the `password_hasher` property.  # noqa: E501

        :param password_digest: The password_digest of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._password_digest = password_digest

    @property
    def password_hasher(self):
        """Gets the password_hasher of this UsersUserIdBody.  # noqa: E501

        The hashing algorithm that was used to generate the password digest. The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [md5](https://en.wikipedia.org/wiki/MD5), pbkdf2_sha256, [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [phpass](https://www.openwall.com/phpass/), [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/), [sha256](https://en.wikipedia.org/wiki/SHA-2) and the [argon2](https://argon2.online/) variants argon2i and argon2id.  If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).  Note: for password hashers considered insecure (at this moment MD5 and SHA256), the corresponding user password hashes will be transparently migrated to Bcrypt (a secure hasher) upon the user's first successful password sign in. Insecure schemes are marked with `(insecure)` in the list below.  Each of the supported hashers expects the incoming digest to be in a particular format. Specifically:  **bcrypt:** The digest should be of the following form:  `$<algorithm version>$<cost>$<salt & hash>`  **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The format should be as follows (as exported from Django):  `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`  **md5** (insecure): The digest should follow the regular form e.g.:  `5f4dcc3b5aa765d61d8327deb882cf99`  **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as follows:  `pbkdf2_sha256$<iterations>$<salt>$<hash>`  Note: Both the salt and the hash are expected to be base64-encoded.  **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following format (as exported from Django):  `pbkdf2_sha256$<iterations>$<salt>$<hash>`  Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.  **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences: 1. uses sha1 instead of sha256 2. accepts the hash as a hex-encoded string  The format is the following:  `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`  **phpass:** Portable public domain password hashing framework for use in PHP applications. Digests hashed with phpass have the following sections:  The format is the following:  `$P$<rounds><salt><encoded-checksum>`  - $P$ is the prefix used to identify phpass hashes. - rounds is a single character encoding a 6-bit integer representing the number of rounds used. - salt is eight characters drawn from [./0-9A-Za-z], providing a 48-bit salt. - checksum is 22 characters drawn from the same set, encoding the 128-bit checksum with MD5.  **scrypt_firebase:** The Firebase-specific variant of scrypt. The value is expected to have 6 segments separated by the $ character and include the following information:  _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase. _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user. _signer key:_ The base64 encoded signer key. _salt separator:_ The base64 encoded salt separator. _rounds:_ The number of rounds the algorithm needs to run. _memory cost:_ The cost of the algorithm run  The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase. The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be retrieved from the project's password hash parameters.  Once you have all these, you can combine it in the following format and send this as the digest in order for Clerk to accept it:  `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`  **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:  _version (v):_ The argon version, version 19 is assumed _memory (m):_ The memory used by the algorithm (in kibibytes) _iterations (t):_ The number of iterations to perform _parallelism (p):_ The number of threads to use  Parts are demarcated by the `$` character, with the first part identifying the algorithm variant. The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism). The final part is the actual digest.  `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3QSwnLc`  **argon2id:** See the previous algorithm for an explanation of the formatting.  For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:  `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`  **sha256** (insecure): The digest should be a 64-length hex string, e.g.:  `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`  # noqa: E501

        :return: The password_hasher of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._password_hasher

    @password_hasher.setter
    def password_hasher(self, password_hasher):
        """Sets the password_hasher of this UsersUserIdBody.

        The hashing algorithm that was used to generate the password digest. The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [md5](https://en.wikipedia.org/wiki/MD5), pbkdf2_sha256, [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [phpass](https://www.openwall.com/phpass/), [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/), [sha256](https://en.wikipedia.org/wiki/SHA-2) and the [argon2](https://argon2.online/) variants argon2i and argon2id.  If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).  Note: for password hashers considered insecure (at this moment MD5 and SHA256), the corresponding user password hashes will be transparently migrated to Bcrypt (a secure hasher) upon the user's first successful password sign in. Insecure schemes are marked with `(insecure)` in the list below.  Each of the supported hashers expects the incoming digest to be in a particular format. Specifically:  **bcrypt:** The digest should be of the following form:  `$<algorithm version>$<cost>$<salt & hash>`  **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The format should be as follows (as exported from Django):  `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`  **md5** (insecure): The digest should follow the regular form e.g.:  `5f4dcc3b5aa765d61d8327deb882cf99`  **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as follows:  `pbkdf2_sha256$<iterations>$<salt>$<hash>`  Note: Both the salt and the hash are expected to be base64-encoded.  **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following format (as exported from Django):  `pbkdf2_sha256$<iterations>$<salt>$<hash>`  Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.  **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences: 1. uses sha1 instead of sha256 2. accepts the hash as a hex-encoded string  The format is the following:  `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`  **phpass:** Portable public domain password hashing framework for use in PHP applications. Digests hashed with phpass have the following sections:  The format is the following:  `$P$<rounds><salt><encoded-checksum>`  - $P$ is the prefix used to identify phpass hashes. - rounds is a single character encoding a 6-bit integer representing the number of rounds used. - salt is eight characters drawn from [./0-9A-Za-z], providing a 48-bit salt. - checksum is 22 characters drawn from the same set, encoding the 128-bit checksum with MD5.  **scrypt_firebase:** The Firebase-specific variant of scrypt. The value is expected to have 6 segments separated by the $ character and include the following information:  _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase. _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user. _signer key:_ The base64 encoded signer key. _salt separator:_ The base64 encoded salt separator. _rounds:_ The number of rounds the algorithm needs to run. _memory cost:_ The cost of the algorithm run  The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase. The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be retrieved from the project's password hash parameters.  Once you have all these, you can combine it in the following format and send this as the digest in order for Clerk to accept it:  `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`  **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:  _version (v):_ The argon version, version 19 is assumed _memory (m):_ The memory used by the algorithm (in kibibytes) _iterations (t):_ The number of iterations to perform _parallelism (p):_ The number of threads to use  Parts are demarcated by the `$` character, with the first part identifying the algorithm variant. The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism). The final part is the actual digest.  `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3QSwnLc`  **argon2id:** See the previous algorithm for an explanation of the formatting.  For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:  `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`  **sha256** (insecure): The digest should be a 64-length hex string, e.g.:  `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`  # noqa: E501

        :param password_hasher: The password_hasher of this UsersUserIdBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["argon2i", "argon2id", "bcrypt", "bcrypt_sha256_django", "md5", "pbkdf2_sha256", "pbkdf2_sha256_django", "pbkdf2_sha1", "phpass", "scrypt_firebase", "sha256"]  # noqa: E501
        if password_hasher not in allowed_values:
            raise ValueError(
                "Invalid value for `password_hasher` ({0}), must be one of {1}"  # noqa: E501
                .format(password_hasher, allowed_values)
            )

        self._password_hasher = password_hasher

    @property
    def skip_password_checks(self):
        """Gets the skip_password_checks of this UsersUserIdBody.  # noqa: E501

        Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`.  # noqa: E501

        :return: The skip_password_checks of this UsersUserIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._skip_password_checks

    @skip_password_checks.setter
    def skip_password_checks(self, skip_password_checks):
        """Sets the skip_password_checks of this UsersUserIdBody.

        Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`.  # noqa: E501

        :param skip_password_checks: The skip_password_checks of this UsersUserIdBody.  # noqa: E501
        :type: bool
        """

        self._skip_password_checks = skip_password_checks

    @property
    def sign_out_of_other_sessions(self):
        """Gets the sign_out_of_other_sessions of this UsersUserIdBody.  # noqa: E501

        Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`.  # noqa: E501

        :return: The sign_out_of_other_sessions of this UsersUserIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._sign_out_of_other_sessions

    @sign_out_of_other_sessions.setter
    def sign_out_of_other_sessions(self, sign_out_of_other_sessions):
        """Sets the sign_out_of_other_sessions of this UsersUserIdBody.

        Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`.  # noqa: E501

        :param sign_out_of_other_sessions: The sign_out_of_other_sessions of this UsersUserIdBody.  # noqa: E501
        :type: bool
        """

        self._sign_out_of_other_sessions = sign_out_of_other_sessions

    @property
    def totp_secret(self):
        """Gets the totp_secret of this UsersUserIdBody.  # noqa: E501

        In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it. Please note that currently the supported options are: * Period: 30 seconds * Code length: 6 digits * Algorithm: SHA1  # noqa: E501

        :return: The totp_secret of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._totp_secret

    @totp_secret.setter
    def totp_secret(self, totp_secret):
        """Sets the totp_secret of this UsersUserIdBody.

        In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it. Please note that currently the supported options are: * Period: 30 seconds * Code length: 6 digits * Algorithm: SHA1  # noqa: E501

        :param totp_secret: The totp_secret of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._totp_secret = totp_secret

    @property
    def backup_codes(self):
        """Gets the backup_codes of this UsersUserIdBody.  # noqa: E501

        If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them. You must provide the backup codes in plain format or the corresponding bcrypt digest.  # noqa: E501

        :return: The backup_codes of this UsersUserIdBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._backup_codes

    @backup_codes.setter
    def backup_codes(self, backup_codes):
        """Sets the backup_codes of this UsersUserIdBody.

        If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them. You must provide the backup codes in plain format or the corresponding bcrypt digest.  # noqa: E501

        :param backup_codes: The backup_codes of this UsersUserIdBody.  # noqa: E501
        :type: list[str]
        """

        self._backup_codes = backup_codes

    @property
    def public_metadata(self):
        """Gets the public_metadata of this UsersUserIdBody.  # noqa: E501

        Metadata saved on the user, that is visible to both your Frontend and Backend APIs  # noqa: E501

        :return: The public_metadata of this UsersUserIdBody.  # noqa: E501
        :rtype: object
        """
        return self._public_metadata

    @public_metadata.setter
    def public_metadata(self, public_metadata):
        """Sets the public_metadata of this UsersUserIdBody.

        Metadata saved on the user, that is visible to both your Frontend and Backend APIs  # noqa: E501

        :param public_metadata: The public_metadata of this UsersUserIdBody.  # noqa: E501
        :type: object
        """

        self._public_metadata = public_metadata

    @property
    def private_metadata(self):
        """Gets the private_metadata of this UsersUserIdBody.  # noqa: E501

        Metadata saved on the user, that is only visible to your Backend API  # noqa: E501

        :return: The private_metadata of this UsersUserIdBody.  # noqa: E501
        :rtype: object
        """
        return self._private_metadata

    @private_metadata.setter
    def private_metadata(self, private_metadata):
        """Sets the private_metadata of this UsersUserIdBody.

        Metadata saved on the user, that is only visible to your Backend API  # noqa: E501

        :param private_metadata: The private_metadata of this UsersUserIdBody.  # noqa: E501
        :type: object
        """

        self._private_metadata = private_metadata

    @property
    def unsafe_metadata(self):
        """Gets the unsafe_metadata of this UsersUserIdBody.  # noqa: E501

        Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.  # noqa: E501

        :return: The unsafe_metadata of this UsersUserIdBody.  # noqa: E501
        :rtype: object
        """
        return self._unsafe_metadata

    @unsafe_metadata.setter
    def unsafe_metadata(self, unsafe_metadata):
        """Sets the unsafe_metadata of this UsersUserIdBody.

        Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.  # noqa: E501

        :param unsafe_metadata: The unsafe_metadata of this UsersUserIdBody.  # noqa: E501
        :type: object
        """

        self._unsafe_metadata = unsafe_metadata

    @property
    def delete_self_enabled(self):
        """Gets the delete_self_enabled of this UsersUserIdBody.  # noqa: E501

        If true, the user can delete themselves with the Frontend API.  # noqa: E501

        :return: The delete_self_enabled of this UsersUserIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._delete_self_enabled

    @delete_self_enabled.setter
    def delete_self_enabled(self, delete_self_enabled):
        """Sets the delete_self_enabled of this UsersUserIdBody.

        If true, the user can delete themselves with the Frontend API.  # noqa: E501

        :param delete_self_enabled: The delete_self_enabled of this UsersUserIdBody.  # noqa: E501
        :type: bool
        """

        self._delete_self_enabled = delete_self_enabled

    @property
    def create_organization_enabled(self):
        """Gets the create_organization_enabled of this UsersUserIdBody.  # noqa: E501

        If true, the user can create organizations with the Frontend API.  # noqa: E501

        :return: The create_organization_enabled of this UsersUserIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._create_organization_enabled

    @create_organization_enabled.setter
    def create_organization_enabled(self, create_organization_enabled):
        """Sets the create_organization_enabled of this UsersUserIdBody.

        If true, the user can create organizations with the Frontend API.  # noqa: E501

        :param create_organization_enabled: The create_organization_enabled of this UsersUserIdBody.  # noqa: E501
        :type: bool
        """

        self._create_organization_enabled = create_organization_enabled

    @property
    def created_at(self):
        """Gets the created_at of this UsersUserIdBody.  # noqa: E501

        A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`).  # noqa: E501

        :return: The created_at of this UsersUserIdBody.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UsersUserIdBody.

        A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`).  # noqa: E501

        :param created_at: The created_at of this UsersUserIdBody.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UsersUserIdBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsersUserIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
