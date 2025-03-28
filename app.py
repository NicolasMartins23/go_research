import streamlit as st
from gene_research import research

def main() -> None:
    """Main function to run the Streamlit app."""
    st.title("GO Term Enrichment Analysis")

    # Sidebar for menu selection
    menu_options: dict[str] = {
        "research": ":microscope: GO Research",
    }

    # Add the options to the sidebar
    menu = st.sidebar.radio("Choose an option", (menu_options["research"]))

    genes_list: list[str] = []

    if menu == menu_options["research"]:
        # User manually enters gene symbols
        genes_input = st.sidebar.text_area("Enter gene symbols (comma-separated)", "")

        # Show the submit button after input field
        submit_button = st.sidebar.button("SUBMIT", type="primary")

        if submit_button:
            # Convert input genes to a list only when button is clicked
            genes_list = [gene.strip() for gene in genes_input.split(",")]

            if genes_list:
                st.write("### Gene Symbols Entered", genes_list)

                results = research(genes_list=genes_list)

                # Show results in the main panel
                st.write("### Enrichment Results", results)
        else:
            st.subheader("How to use?")
            st.write('Type a gene standardize symbol and click "Subtmit" to start the Gene Ontology research')

    spacer = st.sidebar.html("<hr>")
    link_url = "https://bioapps.org/gene-ontology-a-linguagem-universal-dos-genes/"  # Replace with the desired URL
    st.sidebar.markdown(f"[:arrow_upper_right: Read our article about Gene Ontology]({link_url})", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
