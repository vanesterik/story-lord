from main import format_response


def test_format_response():
    # Test case 1: Short content
    content = "Hello, world!"
    expected_output = "\nHello, world!\n"
    assert format_response(content) == expected_output

    # Test case 2: Long content
    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam."
    expected_output = "\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis\nunde omnis iste natus error sit voluptatem accusantium doloremque laudantium,\ntotam rem aperiam.\n"
    assert format_response(content) == expected_output

    # Test case 3: Empty content
    content = ""
    expected_output = "\n\n"
    assert format_response(content) == expected_output

    print("All test cases pass")


test_format_response()
