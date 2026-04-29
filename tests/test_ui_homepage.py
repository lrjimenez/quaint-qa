

def test_open_example_page(page):
        page.goto("https://www.quaintrelle.ai")
        assert "quaintrelleAI" in page.title()
