import streamlit as st

# Page configuration with a professional look.
st.set_page_config(page_title="Bio Agent Launchpad", layout="wide", initial_sidebar_state="auto")

# Inject custom CSS for a dark theme.
dark_theme_css = """
<style>
/* Overall background and text color */
.stApp {
    background-color: #121212;
    color: #e0e0e0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
}

/* Links */
a {
    color: #1e90ff;
}

/* Markdown paragraphs */
.stMarkdown p {
    color: #e0e0e0;
}

/* Ensure sidebar and other elements follow the dark theme */
.css-1d391kg, .css-18e3th9 {
    background-color: #121212 !important;
}
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)

# Title and Introduction
st.title("BADDIE Agent Resource Hub")
st.markdown("### The De Facto Agent Framework for Biology")
st.write("""
Welcome to the BADDIE Agent resource hub. Here, we are aggregating all the open‐source tools, libraries, datasets, and resources available to agent builders. Whether you’re an experienced researcher or just starting out, BADDIE provides a curated collection of components to prototype, experiment, and innovate in the realm of therapeutically motivated bio discovery.
""")

# Define resource categories with an extensive list of resources.
resources = {
    "Core Libraries & Frameworks": [
        {
            "name": "RDKit",
            "description": "Industry-standard toolkit for cheminformatics; makes molecular structures machine-readable.",
            "url": "https://github.com/rdkit/rdkit",
        },
        {
            "name": "Pandas",
            "description": "Powerful Python library for data manipulation and cleaning.",
            "url": "https://pandas.pydata.org/",
        },
        {
            "name": "TorchDrug",
            "description": "Unified machine learning platform for drug discovery with pre-built/trained models.",
            "url": "https://torchdrug.ai",
        },
        {
            "name": "PyTorch Geometric",
            "description": "The go-to library for building Graph Neural Networks for molecular property prediction.",
            "url": "https://github.com/pyg-team/pytorch_geometric",
        },
        {
            "name": "Awesome Cheminformatics",
            "description": "A curated list of high-quality cheminformatics tools and libraries.",
            "url": "https://github.com/hsiaoyi0504/awesome-cheminformatics",
        },
    ],
    "AI/ML & Modeling Tools": [
        {
            "name": "BioBERT",
            "description": "Pre-trained language model for biomedical text mining. See [GitHub](https://github.com/dmis-lab/biobert).",
            "url": "https://github.com/dmis-lab/biobert",
        },
        {
            "name": "BioGPT",
            "description": "Generative pre-trained model tailored for biomedical language understanding. See [GitHub](https://github.com/microsoft/BioGPT).",
            "url": "https://github.com/microsoft/BioGPT",
        },
        {
            "name": "NVIDIA NIM Agent Blueprints",
            "description": "Blueprints for developing and deploying custom AI agents with biological applications.",
            "url": "https://nvidianews.nvidia.com/news/nvidia-and-global-partners-launch-nim-agent-blueprints-for-enterprises-to-make-their-own-ai",
        },
        {
            "name": "SE(3) Diffusion",
            "description": "A diffusion model implementation for 3D structure generation.",
            "url": "https://github.com/jasonkyuyim/se3_diffusion",
        },
        {
            "name": "GeoLDM",
            "description": "Geometric latent diffusion model for structure-based generation tasks.",
            "url": "https://github.com/MinkaiXu/GeoLDM",
        },
    ],
    "Datasets & Knowledge Sources": [
        {
            "name": "CAMEL Biology Dataset",
            "description": "A highly curated dataset for training LLMs in the biological sciences.",
            "url": "https://huggingface.co/datasets/camel-ai/biology",
        },
        {
            "name": "ChEMBL",
            "description": "Gold-standard database of bioactive molecules with drug-like properties.",
            "url": "https://www.ebi.ac.uk/chembl/",
        },
        {
            "name": "DrugAge",
            "description": "Comprehensive database tracking genes and compounds associated with aging.",
            "url": "https://genomics.senescence.info/genes/index.html",
        },
        {
            "name": "TD Commons",
            "description": "A suite of accessible drug discovery datasets (pip installable, ready-to-use).",
            "url": "https://tdcommons.ai",
        },
    ],
    "Pre-trained Models & Pipelines": [
        {
            "name": "AlphaFold3",
            "description": "DeepMind’s protein structure prediction system with a comprehensive setup guide.",
            "url": "https://github.com/google-deepmind/alphafold3/blob/main/docs/installation.md",
        },
        {
            "name": "Biology for AI",
            "description": "AstraZeneca's guide bridging biological concepts with AI applications.",
            "url": "https://github.com/AstraZeneca/biology-for-ai",
        },
        {
            "name": "Bioagents",
            "description": "Framework for building bio agents by integrating multiple bioinformatics tools.",
            "url": "https://github.com/sorgerlab/bioagents",
        },
        {
            "name": "AZ Knowledge Graphs",
            "description": "A curated collection of resources for implementing knowledge graphs in drug discovery.",
            "url": "https://github.com/AstraZeneca/awesome-drug-discovery-knowledge-graphs",
        },
    ],
    "Genomics & Biological Data": [
        {
            "name": "GenBank",
            "description": "NCBI’s genetic sequence database.",
            "url": "https://www.ncbi.nlm.nih.gov/genbank/",
        },
        {
            "name": "RefSeq",
            "description": "NCBI Reference Sequence Database for genomes, transcripts, and proteins.",
            "url": "https://www.ncbi.nlm.nih.gov/refseq/",
        },
        {
            "name": "ENCODE",
            "description": "The Encyclopedia of DNA Elements project.",
            "url": "https://www.encodeproject.org/",
        },
        {
            "name": "1000 Genomes",
            "description": "An international project providing a comprehensive resource on human genetic variation.",
            "url": "https://www.internationalgenome.org/",
        },
        {
            "name": "GTEx",
            "description": "Genotype-Tissue Expression project for studying tissue-specific gene expression.",
            "url": "https://gtexportal.org/",
        },
    ],
    "Protein Structures & Pathways": [
        {
            "name": "PDB",
            "description": "The Protein Data Bank: a repository for 3D structural data of biological molecules.",
            "url": "https://www.rcsb.org/",
        },
        {
            "name": "UniProt",
            "description": "Comprehensive resource for protein sequence and functional information.",
            "url": "https://www.uniprot.org/",
        },
        {
            "name": "AlphaFold DB",
            "description": "Database of protein structure predictions from AlphaFold.",
            "url": "https://alphafold.ebi.ac.uk/",
        },
        {
            "name": "InterPro",
            "description": "Integrative resource for protein families, domains, and functional sites.",
            "url": "https://www.ebi.ac.uk/interpro/",
        },
        {
            "name": "SWISS-MODEL",
            "description": "Automated protein structure homology-modeling server.",
            "url": "https://swissmodel.expasy.org/",
        },
        {
            "name": "KEGG",
            "description": "Database resource for understanding high-level functions of biological systems.",
            "url": "https://www.genome.jp/kegg/",
        },
        {
            "name": "Reactome",
            "description": "Curated database of pathways and reactions in human biology.",
            "url": "https://reactome.org/",
        },
        {
            "name": "BioCyc",
            "description": "Collection of pathway/genome databases.",
            "url": "https://biocyc.org/",
        },
        {
            "name": "STRING",
            "description": "Database of known and predicted protein–protein interactions.",
            "url": "https://string-db.org/",
        },
        {
            "name": "BioGRID",
            "description": "Repository for protein and genetic interactions.",
            "url": "https://thebiogrid.org/",
        },
    ],
    "Literature & Research Resources": [
        {
            "name": "PubMed",
            "description": "Search engine accessing primarily the MEDLINE database of references and abstracts on life sciences.",
            "url": "https://pubmed.ncbi.nlm.nih.gov/",
        },
        {
            "name": "Europe PMC",
            "description": "Biomedical literature and life science research database.",
            "url": "https://europepmc.org/",
        },
        {
            "name": "bioRxiv",
            "description": "Preprint server for biology.",
            "url": "https://www.biorxiv.org/",
        },
        {
            "name": "ScienceDirect",
            "description": "Leading full-text scientific database offering journal articles and book chapters.",
            "url": "https://www.sciencedirect.com/",
        },
        {
            "name": "Google Scholar",
            "description": "Broadly searches scholarly literature across many disciplines.",
            "url": "https://scholar.google.com/",
        },
    ],
    "Research Papers & Articles": [
        {
            "name": "Nature Methods Article",
            "description": "Research article detailing novel methods in biology. [Link]",
            "url": "https://www.nature.com/articles/s41592-023-02086-5",
        },
        {
            "name": "ArXiv Paper (Diffusion Models)",
            "description": "Recent preprint on diffusion models in 3D structure generation.",
            "url": "https://arxiv.org/abs/2409.13740",
        },
        {
            "name": "ArXiv Paper (Bio Discovery)",
            "description": "Preprint discussing advanced methodologies in biological discovery.",
            "url": "https://arxiv.org/abs/2304.053761",
        },
        {
            "name": "Wiley Article",
            "description": "Article from *Clinical Pharmacology & Therapeutics* discussing drug discovery approaches.",
            "url": "https://ascpt.onlinelibrary.wiley.com/doi/epdf/10.1002/cpt.3542",
        },
    ],
    "Other Tools & Resources": [
        {
            "name": "Future House Aviary",
            "description": "Research announcements and innovative projects in biosciences.",
            "url": "https://www.futurehouse.org/research-announcements/aviary",
        },
        {
            "name": "InstaDeep Open Resources",
            "description": "Suite of open-source AI tools and platforms specializing in biological applications.",
            "url": "https://www.instadeep.com/open/",
        },
        {
            "name": "Future House About",
            "description": "Learn more about Future House and their initiatives in the bio space.",
            "url": "https://www.futurehouse.org/about",
        },
    ],
}

# Function to render each resource category.
def render_category(category, items):
    st.header(category)
    for item in items:
        st.markdown(f"**[{item['name']}]({item['url']})** - {item['description']}")
    st.markdown("---")

# Render each resource category.
for category, items in resources.items():
    render_category(category, items)

# Additional Section: Standard Bio Agent Pipeline
st.markdown("## Standard Bio Agent Pipeline")
st.markdown("""
A typical pipeline using these resources might include:

1. **Data Ingestion & Cleaning:**  
   - Use **Pandas** to process and clean data from sources such as GenBank, ChEMBL, or the CAMEL Biology Dataset.

2. **Feature Extraction & Molecule Processing:**  
   - **RDKit** transforms raw molecular data into machine-interpretable features.  
   - **TorchDrug** and **PyTorch Geometric** facilitate the development of graph-based models.

3. **Model Building & Inference:**  
   - Train models using **PyTorch** and leverage pre-trained tools (e.g., BioBERT, BioGPT) for domain-specific predictions.  
   - Use frameworks like **TorchDrug** for rapid prototyping of property predictors.

4. **Iterative Reasoning & Optimization:**  
   - Integrate an LLM-based agent (e.g., built on top of ELIZA) to analyze and suggest molecular modifications based on predictive outputs.  
   - Iterate to refine molecular structures and enhance properties.

5. **Deployment:**  
   - Package and deploy your complete pipeline on cloud platforms (e.g., AWS EC2) for scalable experimentation and public interfacing.
""")

# Footer / Next Steps
st.markdown("## Roadmap & Community")
st.markdown("""
- **First Release:** BADDIE educational launchpad and resource hub (launched 2/5/25).  
- **Agent Release:** Launch agents built on our proprietary graph-RAG knowledge base that unifies major protein, chemistry, and drug databases. Demonstrate a full pipeline (data → RDKit → model → iterative reasoning) on compelling use cases.  
- **BADDIE Platform Release:** Introduce the BADDIE platform, a suite of tools and libraries for building bio agents.  
- **Tokenized Agent Support:** Enable launching your own agents with tokens paired against $DRUGS, available for a fee.

Join our community to contribute, provide feedback, or stay updated on future releases!
""")
