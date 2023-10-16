from django.urls import reverse


class TestIndexOcLettingsSiteView:
    """Integration tests for oc_lettings_site index view."""

    def test_index_view(self, client):
        """
        GIVEN a path to site index
        WHEN the '/oc_lettings_site' page is requested (GET)
        THEN checks that response is 200, the correct template is used and site title is displayed
        """
        url = reverse("oc_lettings_site:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "oc_lettings_site/index.html" in [
            template.name for template in response.templates
        ]
        assert "Welcome to Holiday Homes" in str(response.content)

    def test_custom_404_view(self, client):
        """
        GIVEN a wrong path
        WHEN page is requested (GET)
        THEN checks that response is 404, correct template is used and PAGE NOT FOUND is displayed
        """
        response = client.get("/non_existent_path")
        assert response.status_code == 404
        assert "404.html" in [t.name for t in response.templates]
        assert "PAGE NOT FOUND" in str(response.content)
