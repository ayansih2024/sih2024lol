import streamlit as st
import re

# Set page title and layout
st.set_page_config(page_title="Your Chatbot UI", layout="wide")

# Declare the rules_responses dictionary
rules_responses = {
    r'(mines)': 'Mining in India is regulated by the Mines and Minerals (Development and Regulation) Act, 1957. It covers the development and regulation of mines and the conservation of minerals.',
    r'(rules|regulations)': 'The rules and regulations for mining in India are primarily outlined in the Mines and Minerals (Development and Regulation) Act, 1957. This includes guidelines on grant of leases, royalty rates, and environmental clearances.',
    r'(lease)': 'Mining leases in India are granted under the Mines and Minerals (Development and Regulation) Act, 1957, and its subsequent amendments. The lease grants the holder the right to mine specified minerals within the defined area for a specific duration.',
    r'(environmental impact|environment)': 'Mining activities in India are subject to environmental regulations. The Environmental Impact Assessment (EIA) process is crucial for obtaining clearances. It assesses and mitigates potential environmental impacts.',
    r'(foreign investment|international investment)': 'Foreign investment in mining projects is regulated by the Foreign Exchange Management Act (FEMA) and is subject to government approval. Specific guidelines exist to govern the participation of foreign entities in the mining sector.',
    r'(safety measures|safety regulations)': 'Safety measures for mining operations in India are mandated under the Mines Act, 1952. These measures include provisions for the health and safety of workers, prevention of accidents, and emergency response planning.',
    r'(Ministry of Mines)': 'The Ministry of Mines in India formulates policies and legislation related to mining. It oversees the implementation of mining laws, promotes sustainable development, and addresses issues within the mining sector.',
    r'(small-scale mining|artisanal mining)': 'Artisanal and small-scale mining in India is governed by specific guidelines that aim to regulate and support these activities. The Ministry of Mines has issued guidelines to ensure responsible and sustainable practices.',
    r'(duration of mining lease)': 'The duration of a mining lease in India varies based on the mineral being mined. Generally, it can range from 20 to 50 years. The leaseholder must comply with all relevant regulations during this period.',
    r'(royalty calculation|mineral royalty)': 'Royalty for minerals extracted during mining is calculated based on the specific mineral, its grade, and the method of extraction. The rates are determined by the government and are subject to periodic revisions.',
    r'(ecologically sensitive areas)': 'Mining in ecologically sensitive areas is subject to stringent regulations. Clearances from the Ministry of Environment, Forest and Climate Change (MoEFCC) are required, and additional measures may be mandated to protect the environment.',
    r'(environmental clearance process)': 'The environmental clearance process involves a detailed Environmental Impact Assessment (EIA) study. It includes public consultations, scrutiny by expert committees, and approval from the Ministry of Environment, Forest and Climate Change (MoEFCC).',
    r'(mining reforms)': 'Mining reforms in India aim to streamline processes, enhance transparency, and attract investments. Reforms may include changes in auction mechanisms, exploration policies, and efforts to address industry challenges.',
    r'(dispute resolution|mining lease disputes)': 'Disputes related to mining leases are typically resolved through legal mechanisms, including arbitration and the judiciary. The Mines and Minerals (Development and Regulation) Act provides a framework for dispute resolution.',
    r'(rehabilitation and resettlement)': 'Provisions for the rehabilitation and resettlement of communities affected by mining are outlined in the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement (RFCTLARR) Act, 2013.',
    r'(illegal mining|preventing illegal mining)': 'Preventing illegal mining involves strict enforcement by state authorities, use of technology for monitoring, and community involvement. Penalties for illegal mining are defined in the Mines and Minerals (Development and Regulation) Act.',
    r'(use-it-or-lose-it|mining lease terms)': 'The "use-it-or-lose-it" principle implies that mining leaseholders must actively engage in mining activities. Failure to do so may result in the cancellation or non-renewal of the mining lease.',
    r'(National Mineral Exploration Policy)': 'The National Mineral Exploration Policy aims to promote mineral exploration and reduce dependency on imports. It encourages private sector participation, technological advancements, and data transparency.',
    r'(mineral classification)': 'Minerals in India are classified based on their economic value and characteristics. The Mines and Minerals (Development and Regulation) Act provides the criteria for classification and categorization of minerals.',
    r'(offshore mining)': 'Offshore mining in India is regulated by the Mines and Minerals (Development and Regulation) Act. Specific guidelines are in place for obtaining leases for offshore areas, including environmental considerations.',
    r'(auction process|mineral block auction)': 'Mineral blocks are auctioned through a transparent process outlined by the government. The auction process involves competitive bidding, and successful bidders are granted mining leases.',
    r'(penalties|non-compliance penalties)': 'Penalties for non-compliance with mining regulations in India can include fines, suspension of mining activities, or cancellation of mining leases. The specific penalties are outlined in the Mines and Minerals (Development and Regulation) Act.',
    r'(mining rights|mining leases)': 'Mining rights generally refer to the legal authority to extract minerals, while mining leases provide exclusive rights for a specified area and duration. Both are governed by the Mines and Minerals (Development and Regulation) Act.',
    r'(allocation of mining leases)': 'The fair and transparent allocation of mining leases is ensured through competitive bidding processes. Auctions are conducted by the government, and the highest bidder is awarded the mining lease.',
    r'(District Mineral Foundation)': 'The District Mineral Foundation (DMF) is established to address the needs of areas affected by mining. It is funded through contributions from mining companies and is used for local development initiatives.',
    r'(criteria for mining lease eligibility)': 'Entities eligible for a mining lease must meet specific criteria, including financial capability, technical expertise, and compliance with environmental and social standards. These criteria aim to ensure responsible mining practices.',
    r'(rare earth minerals)': 'Regulations for rare earth minerals in India involve specific guidelines for exploration, extraction, and processing. These regulations are in line with the overall framework for mining activities.',
    r'(social impact of mining)': 'The government addresses the social impact of mining through various measures, including community engagement, social impact assessments, and the implementation of Corporate Social Responsibility (CSR) initiatives by mining companies.',
    r'(digital initiatives|mining sector)': 'Digital initiatives in the mining sector include the use of technology for data management, monitoring, and automation. These initiatives aim to enhance efficiency, transparency, and decision-making.',
    r'(sustainable mining practices)': 'Efforts to promote sustainable mining practices involve adherence to environmental and social standards, responsible resource management, and the use of eco-friendly technologies in mining operations.',
    r'(mineral transportation regulations)': 'Transportation of minerals from mining sites is subject to regulations to prevent illegal trade and ensure fair practices. Compliance with transportation guidelines is essential for mining companies.',
    r'(tax incentives|mining companies)': 'Tax incentives or exemptions for mining companies may be provided by the government to encourage investments. These incentives could include reduced tax rates, depreciation benefits, or exemptions on specific transactions.',
    r'(Indian Bureau of Mines)': 'The Indian Bureau of Mines (IBM) is a crucial regulatory body overseeing mining operations. It plays a key role in mineral exploration, mine safety, and the enforcement of mining regulations.',
    r'(rehabilitation of abandoned mining sites)': 'The rehabilitation of abandoned mining sites involves restoring the land to its pre-mining state. Mining companies are typically required to set aside funds for post-mining land reclamation and rehabilitation activities.',
    r'(resettlement of mining-affected communities)': 'Resettlement of communities affected by mining is carried out in accordance with the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement (RFCTLARR) Act, 2013.',
    r'(state government role|mining regulation)': 'State governments play a crucial role in regulating mining activities within their jurisdiction. They grant leases, monitor compliance, and may have specific regulations tailored to regional needs.',
    r'(environmental impact assessments|EIAs|mining projects)': 'Environmental Impact Assessments (EIAs) for mining projects involve a comprehensive study of potential environmental impacts. These assessments are critical for obtaining environmental clearances and ensuring sustainable mining practices.',
    r'(precious stones|mining regulations)': 'Regulations for the mining of precious stones, such as diamonds and emeralds, include guidelines for exploration, extraction, and trade. These regulations aim to prevent illegal trade and promote ethical practices.',
    r'(advanced technologies|mining industry)': 'The government promotes the use of advanced technologies in the mining industry to improve efficiency, safety, and environmental sustainability. Technologies such as automation, IoT, and AI are encouraged.',
    r'(prospecting license process|mineral exploration)': 'The process of obtaining a prospecting license for mineral exploration involves submitting an application to the relevant authorities. The license allows the holder to conduct preliminary surveys and assessments to identify mineral deposits.',
    r'(mining waste disposal regulations)': 'Regulations for the disposal of mining waste and tailings aim to minimize environmental impact. Guidelines include safe disposal methods, containment measures, and monitoring to prevent contamination of soil and water.',
    r'(streamlining mining approval process)': 'Efforts to streamline the mining approval process involve simplifying procedures, reducing bureaucratic hurdles, and leveraging technology for faster and more transparent decision-making.'
}

def mining_rules_bot(user_input, selected_keyword):
    responses = []  # Store multiple responses
    for pattern, response in rules_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE) and selected_keyword == pattern:
            responses.append(response)

    if responses:
        return responses  # Return a list of responses

    return ["I'm sorry, I don't have information on that specific topic. Please consult official sources or legal documents for accurate and up-to-date information."]

# Create the Streamlit app
st.title("Miner Mark AI")
chat_history = st.container()

st.markdown("Ask me anything about mining rules in India. I'll try my best to provide helpful information.")

# Create sidebar for keywords
keywords = list(rules_responses.keys())
selected_keyword = st.sidebar.selectbox("Select a keyword", keywords)

user_input = st.text_input("Enter your question:")

if st.button("Enter"):
    if user_input:
        responses = mining_rules_bot(user_input, selected_keyword)
        for i, response in enumerate(responses):
            chat_history.write(f"Chatbot ({i+1}): {response}")
            st.write(f"Chatbot ({i+1}): {response}")
        chat_history.write("You: " + user_input)
