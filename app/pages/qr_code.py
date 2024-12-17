import reflex as rx

from app.components.navbar import navbar
from app.constants.routes import Route
from app.services.qrcode_service import generate_qr_code

DATABASE = [
    {"id": 1, "name": "John Smith"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"},
    {"id": 4, "name": "Michael Smith"},
    {"id": 5, "name": "Robert Brown"},
]

class SearchState(rx.State):
    query: str = ""  # The input query
    results: list[dict] = []  # Results list
    selected_id: int = None  # Stores the selected person's ID
    qr_code_path: str = ""  # Path to the generated QR code image

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the search form submission."""
        search_query = form_data.get("input", "").strip().lower()
        self.query = search_query
        if search_query:
            self.results = [
                person
                for person in DATABASE
                if search_query in person["name"].lower()
            ]
        else:
            self.results = []

    @rx.event
    def handle_clear(self):
        """Clear the search input and results."""
        self.query = ""
        self.results = []
        self.selected_id = None
        self.qr_code_path = ""
        yield rx.set_value("input", "")  # Reset input field

    @rx.event
    def update_query(self, new_value: str):
        """Update the query state with the new value."""
        self.query = new_value.strip().lower()
        # Trigger the search when query is updated
        self.handle_submit({"input": self.query})

    @rx.event
    def select_person(self, person_id: int):
        """Set the selected ID and generate a QR code."""
        self.selected_id = person_id
        # Find the name of the person with the given ID
        person_name = next((person["name"] for person in DATABASE if person["id"] == person_id), "")
        # Generate the QR code
        self.qr_code_path = generate_qr_code(person_id)


@rx.page(route=Route.QRCODE)
def qr_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                navbar(),
                rx.heading("Mitarbeiter Suche"),
                rx.center(
                    rx.form.root(
                        rx.vstack(
                            rx.hstack(
                                rx.input(
                                    name="input",
                                    placeholder="Name eingeben...",
                                    value=SearchState.query,
                                    on_change=SearchState.update_query,
                                    required=True,
                                ),
                                rx.button("Suchen", type="submit"),
                                rx.button(
                                    "Zurücksetzen", on_click=SearchState.handle_clear
                                ),
                                spacing="4",
                            ),
                            width="100%",
                            align_items="center",
                        ),
                        on_submit=SearchState.handle_submit,
                        reset_on_submit=False,
                        align_items="center",
                    ),
                    width="100%",
                ),
                rx.divider(),
                rx.heading("Ergebnisse:"),
                rx.cond(
                    SearchState.results,
                    rx.vstack(
                        rx.foreach(
                            SearchState.results,
                            lambda person: rx.button(
                                person["name"],
                                on_click=lambda p=person: SearchState.select_person(
                                    p["id"]
                                ),
                                color_scheme="blue",
                                variant="ghost",
                            ),
                        ),
                        spacing="2",
                        align_items="start",
                        width="100%",
                    ),
                    rx.text("Keine Ergebnisse gefunden."),
                ),
                # Display selected ID and QR code
                rx.cond(
                    SearchState.selected_id,
                    rx.vstack(
                        rx.text(
                            f"Ausgewählte ID: {SearchState.selected_id}",
                            font_size="md",
                            color="green",
                        ),
                        # Ensure the image src attribute points to a valid image path
                        rx.image(
                            src=f"assets/{SearchState.selected_id}.png",  # Adjust this path to your actual file structure
                            alt="QR Code",
                            width="370px",
                            height="370px",
                        ),
                    ),
                ),
                align_items="center",
                spacing="4",
                width="100%",
            ),
            width="50%",
            padding="4",
        )
    )

