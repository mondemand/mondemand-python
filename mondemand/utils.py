from __future__ import absolute_import, division, print_function, unicode_literals

from typing import Text, Union, Optional

import six


def text_to_cstring(s):
	# type: (Optional[Union[Text, str, bytes]]) -> Optional[bytes]

	if s is None or isinstance(s, six.binary_type):
		return s

	return s.encode()


def cstring_to_text(ffi, s):
	return ffi.string(s).decode()
	## type: (Optional[Union[Text, bytes]]) -> Optional[Text]
	# if s is None or isinstance(s, six.text_type):
	# 	return s


def string_array_to_text_list(ffi, s):
	result = []

	i = 0
	while s[i] != ffi.NULL:
		result.append(cstring_to_text(ffi, s[i]))
		i += 1

	return result
