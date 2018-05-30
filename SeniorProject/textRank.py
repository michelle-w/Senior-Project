'''
Created on May 24, 2018

@author: shobh
'''
# coding: iso-8859-1
from summa import summarizer
from _codecs import decode

# -*- coding: latin-1 -*-


text = """Quantum computing, in which computations are carried out based on the quantum principles of matter, was proposed by American theoretical physicist Richard Feynman in the early 1980s. Unlike normal computer bits, the qubit units used by quantum computers store information in two-state systems, such as electrons or photons, that are considered to be in all possible quantum states at once (a phenomenon known as superposition).
"In classical computing, you write in bits of zero and one," said Thomas Papenbrock, a theoretical nuclear physicist at the University of Tennessee and ORNL who co-led the project with ORNL quantum information specialist Pavel Lougovski. "But with a qubit, you can have zero, one, and any possible combination of zero and one, so you gain a vast set of possibilities to store data."
In October 2017 the multidivisional ORNL team started developing codes to perform simulations on the IBM QX5 and the Rigetti 19Q quantum computers through DOE's Quantum Testbed Pathfinder project, an effort to verify and validate scientific applications on different quantum hardware types. Using freely available pyQuil software, a library designed for producing programs in the quantum instruction language, the researchers wrote a code that was sent first to a simulator and then to the cloud-based IBM QX5 and Rigetti 19Q systems.
The team performed more than 700,000 quantum computing measurements of the energy of a deuteron, the nuclear bound state of a proton and a neutron. From these measurements, the team extracted the deuteron's binding energy -- the minimum amount of energy needed to disassemble it into these subatomic particles. The deuteron is the simplest composite atomic nucleus, making it an ideal candidate for the project.
"Qubits are generic versions of quantum two-state systems. They have no properties of a neutron or a proton to start with," Lougovski said. "We can map these properties to qubits and then use them to simulate specific phenomena -- in this case, binding energy."
A challenge of working with these quantum systems is that scientists must run simulations remotely and then wait for results. ORNL computer science researcher Alex McCaskey and ORNL quantum information research scientist Eugene Dumitrescu ran single measurements 8,000 times each to ensure the statistical accuracy of their results.
"It's really difficult to do this over the internet," McCaskey said. "This algorithm has been done primarily by the hardware vendors themselves, and they can actually touch the machine. They are turning the knobs."
The team also found that quantum devices become tricky to work with due to inherent noise on the chip, which can alter results drastically. McCaskey and Dumitrescu successfully employed strategies to mitigate high error rates, such as artificially adding more noise to the simulation to see its impact and deduce what the results would be with zero noise.
"These systems are really susceptible to noise," said Gustav Jansen, a computational scientist in the Scientific Computing Group at the Oak Ridge Leadership Computing Facility (OLCF), a DOE Office of Science User Facility located at ORNL. "If particles are coming in and hitting the quantum computer, it can really skew your measurements. These systems aren't perfect, but in working with them, we can gain a better understanding of the intrinsic errors."
At the completion of the project, the team's results on two and three qubits were within 2 and 3 percent, respectively, of the correct answer on a classical computer, and the quantum computation became the first of its kind in the nuclear physics community.
The proof-of-principle simulation paves the way for computing much heavier nuclei with many more protons and neutrons on quantum systems in the future. Quantum computers have potential applications in cryptography, artificial intelligence, and weather forecasting because each additional qubit becomes entangled -- or tied inextricably -- to the others, exponentially increasing the number of possible outcomes for the measured state at the end. This very benefit, however, also has adverse effects on the system because errors may also scale exponentially with problem size.
Papenbrock said the team's hope is that improved hardware will eventually enable scientists to solve problems that cannot be solved on traditional high-performance computing resources -- not even on the ones at the OLCF. In the future, quantum computations of complex nuclei could unravel important details about the properties of matter, the formation of heavy elements, and the origins of the universe.
"""

print(summarizer.summarize(text))

text2= """Specifically, the findings shed new light on how stress, depression and other mental states can alter organ function, and show that there is a real anatomical basis for psychosomatic illness. The research also provides a concrete neural substrate that may help explain why meditation and certain exercises such as yoga and Pilates can be so helpful in modulating the body's responses to physical, mental and emotional stress.

"Our results turned out to be much more complex and interesting than we imagined before we began this study," said senior author Peter L. Strick, Ph.D., Thomas Detre Chair of the Department of Neurobiology and scientific director of the University of Pittsburgh Brain Institute.

In their experiments, the scientists traced the neural circuitry that links areas of the cerebral cortex to the adrenal medulla (the inner part of the adrenal gland, which is located above each kidney). The scientific team included lead author Richard P. Dum, Ph.D., research associate professor in the Department of Neurobiology; David J. Levinthal, M.D., Ph.D., assistant professor in the Department of Medicine; and Dr. Strick.

The scientists were surprised by the sheer number of neural networks they uncovered. Other investigators had suspected that one or, perhaps, two cortical areas might be responsible for the control of the adrenal medulla. The actual number and location of the cortical areas were uncertain. In the PNAS study, the Strick laboratory used a unique tracing method that involves rabies virus. This approach is capable of revealing long chains of interconnected neurons. Using this approach, Dr. Strick and his colleagues demonstrated that the control of the adrenal medulla originates from multiple cortical areas. According to the new findings, the biggest influences arise from motor areas of the cerebral cortex and from other cortical areas involved in cognition and affect.

Why does it matter which cortical areas influence the adrenal medulla? Acute responses to stress include a wide variety of changes such as a pounding heart, sweating and dilated pupils. These responses help prepare the body for action and often are characterized as "fight or flight responses." Many situations in modern life call for a more thought-out reaction than simple "fight or flight," and it is clear that we have some cognitive control (or what neuroscientists call "top-down" control) over our responses to stress.

"Because we have a cortex, we have options," said Dr. Strick. "If someone insults you, you don't have to punch them or flee. You might have a more nuanced response and ignore the insult or make a witty comeback. These options are part of what the cerebral cortex provides."

Another surprising result was that motor areas in the cerebral cortex, involved in the planning and performance of movement, provide a substantial input to the adrenal medulla. One of these areas is a portion of the primary motor cortex that is concerned with the control of axial body movement and posture. This input to the adrenal medulla may explain why core body exercises are so helpful in modulating responses to stress. Calming practices such as Pilates, yoga, tai chi and even dancing in a small space all require proper skeletal alignment, coordination and flexibility.

The PNAS study also revealed that the areas of the cortex that are active when we sense conflict, or are aware that we have made an error, are a source of influence over the adrenal medulla. "This observation," said Dr. Strick, "raises the possibility that activity in these cortical areas when you re-imagine an error, or beat yourself up over a mistake, or think about a traumatic event, results in descending signals that influence the adrenal medulla in just the same way as the actual event." These anatomical findings have relevance for therapies that deal with post-traumatic stress.

Additional links with the adrenal medulla were discovered in cortical areas that are active during mindful mediation and areas that show changes in bipolar familial depression. "One way of summarizing our results is that we may have uncovered the stress and depression connectome," says Dr. Strick.

Overall, these results indicate that circuits exist to link movement, cognition and affect to the function of the adrenal medulla and the control of stress. This circuitry may mediate the effects of internal states like chronic stress and depression on organ function and, thus, provide a concrete neural substrate for some psychosomatic illness."""

print()
print(summarizer.summarize(text2, ratio=0.1))

text3 = """Alzheimers disease (AD) is a neurodegenerative, fatal brain disease characterized by impairments in memory, language, reasoning, and cognition. Identifying AD in its earliest stages of Mild Cognitive Impairment (MCI) allows patients access to the best possible treatments, and time to make crucial caregiving and financial decisions. Currently, no accurate diagnostic tests exist for early-stage AD; internationally just one in four patients are diagnosed. In this study, the development of a machine learning tool to accurately diagnose AD and identify high-risk MCI patients is proposed, using neuropsychological and blood proteomic profiles. A novel two-layer hierarchical framework was designed: The first layer diagnoses patients as healthy, MCI, or AD, and the second layer analyzes healthy/MCI patient profiles to predict future AD onset. The online Alzheimers Neuroimaging Initiative database of 560 patients was used to build the first model. A subset of 368 patients was used for the second model, using multiple observations per patient across a 12-month time-span. For each classification layer, a multi-pronged approach was developed to extract the most relevant biomarker data from patient profiles, integrating univariate and multivariate methods. Upon evaluation, the first model diagnosed patients with a 91% accuracy, based on linear components extracted from proteomic profiles. The second model predicted future AD onset for current MCI patients with a 92% ROC accuracy within a 6-48-month timeframe, using biomarkers selected from both proteomic and neuropsychological profiles. These results far outperform prior research and indicate that this tool will provide a low-cost, minimally invasive method of detecting early-onset AD."""
print()
print(summarizer.summarize(text3, ratio=0.2))


file4 = open("articles/testArticle3.txt", mode="rt")
text4=file4.read()
print()
print(summarizer.summarize(text4, ratio=0.001))

print(text4)
