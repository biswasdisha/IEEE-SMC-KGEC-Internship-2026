The rapid growth of speech technologies has created new opportunities for extracting structured information from recorded interviews. However, transforming long-duration, regional-language speech into reliable research insights remains challenging because of limited language resources, linguistic variation, code-switching, API constraints, and the mismatch between speech-recognition accuracy and downstream research usefulness. This paper presents a multilingual speech-to-insight framework that investigates the complete processing pipeline from long-duration Bengali interview audio to semantic research outputs. Bengali is used as the experimental case because it is among the world's most widely spoken languages, while Bengali speech-processing systems continue to face challenges associated with dialectal variation, pronunciation differences, limited annotated resources, and multilingual usage. Ethnologue places Bengali among the world's ten most spoken languages.
The proposed framework evaluates the use of different model classes for different processing tasks rather than treating a single model as sufficient for the complete workflow. Sarvam AI is employed for Bengali automatic speech recognition because its speech-to-text service explicitly supports Bengali (bn-IN) and multiple Indian languages. The resulting Bengali transcript is translated into English to enable downstream analysis using established multilingual NLP models. XLM-RoBERTa is employed for sentiment analysis because it was pretrained across 100 languages and demonstrated strong cross-lingual transfer, including improvements for low-resource languages. KeyBERT is used for semantic keyword extraction because it identifies candidate words and phrases according to their embedding similarity with the document.
The framework specifically addresses long-audio processing by segmenting a 1,143.51-second agricultural interview into 40 approximately 29-second segments before sequential speech recognition. The experimental pipeline produced a Bengali transcript, English translation, sentiment classification, and ranked semantic keywords. The implemented sentiment model classified the analyzed text as negative with a confidence score of 0.417, while ten keywords were extracted.
Rather than evaluating the system solely using transcription accuracy, this study proposes a Research Utility Score (RUS) that combines transcription quality, semantic fidelity, narrative extraction, evidence grounding, processing efficiency, and reproducibility. The framework is intended not only as an implementation but also as a benchmarking methodology for future researchers comparing commercial APIs and open-source speech-recognition models such as Whisper under regional-language and code-mixed conditions.
Keywords: Multilingual Speech Processing, Bengali ASR, Long-Duration Audio, Code-Switching, Sarvam AI, Whisper, XLM-RoBERTa, KeyBERT, Sentiment Analysis, Keyword Extraction, Low-Resource Languages, Research Utility Score.
________________________________________
1. Introduction
1.1 Background
Speech is one of the most natural forms of human communication, and recorded interviews contain valuable information for qualitative research. In fields such as agriculture, climate adaptation, governance, education, and social science, interviews can contain detailed information that is difficult to obtain through structured datasets alone.
However, the value of recorded interviews is often limited by the effort required to process them. A researcher must listen to the recording, transcribe the speech, identify important statements, translate the content when necessary, identify themes, and interpret the findings. For a long interview, these activities must be repeated across thousands of words and multiple speakers.
Manual transcription is therefore not simply inconvenient. It creates a scalability problem. As the number and duration of interviews increase, the time required for transcription and qualitative coding also increases. It can delay analysis, increase researcher workload, and make large-scale qualitative studies difficult to conduct consistently.
Artificial Intelligence provides a potential solution by automating several stages of this workflow. Automatic Speech Recognition can convert speech into text, while Natural Language Processing can identify sentiment, keywords, themes, and other semantic information.
However, multilingual speech creates an additional challenge.
Bengali is one of the world's most widely spoken languages and is ranked among the ten most spoken languages in Ethnologue's global language ranking. Yet real-world Bengali speech is not necessarily standardized. Speakers may use regional pronunciation, informal vocabulary, English technical terms, and code-mixed expressions.
For example, the experimental interview contains Bengali speech mixed with terms such as:
•	agriculture;
•	weather;
•	extreme heat;
•	water logging;
•	market;
•	soil testing;
•	technology;
•	AI;
•	IoT;
•	real time.
The transcript therefore represents a realistic conversational environment rather than a controlled Bengali speech dataset.
This motivates the development of a framework that evaluates not only whether speech can be transcribed, but whether the resulting output can actually support research.
________________________________________
2. Problem Statement
The central problem addressed in this study is:
How can long-duration, multilingual Bengali interview recordings be processed through an AI pipeline that is both technically efficient and useful for downstream qualitative research?
The problem contains five interconnected challenges.
2.1 Long-Duration Audio
Speech-recognition services may impose duration or request constraints. Sending an entire interview as a single request can therefore result in failed requests, timeouts, or processing difficulties.
The experimental recording in this study lasted 1,143.51 seconds. Instead of processing the entire recording as one input, the system divided it into 40 approximately 29-second segments.
2.2 Linguistic Diversity
Bengali speech can contain pronunciation variation, regional vocabulary, informal speech, and code-switching. These characteristics create challenges for ASR systems trained primarily on standardized or high-resource speech.
2.3 Model Selection
Different AI models have different strengths.
An ASR model is designed to recognize speech. A translation model is designed to transfer meaning between languages. A sentiment model is designed to classify polarity. A keyword-extraction system identifies semantically important terms.
Therefore, the research question should not be:
“Which single AI model can analyze the entire interview?”
Instead, it should be:
“Which combination of specialized models produces the most useful end-to-end research output?”
2.4 Downstream Error Propagation
Errors introduced during ASR can propagate into translation and NLP stages:
[
Audio \rightarrow ASR \rightarrow Translation \rightarrow NLP
]
An incorrect word can therefore affect the translated meaning, sentiment classification, or keyword extraction.
2.5 Research Utility
A transcript can contain word-level errors while still preserving the central meaning of an interview. Conversely, a transcript with apparently acceptable word accuracy may fail to identify important themes.
Therefore, WER and CER alone cannot completely represent the usefulness of the system.
________________________________________
3. Research Questions
This study investigates the following questions:
RQ1
How effectively can a long-duration Bengali interview be processed through sequential audio segmentation and automatic speech recognition?
RQ2
How do linguistic characteristics such as code-switching and domain-specific vocabulary affect the speech-to-text pipeline?
RQ3
Why should different models be selected for speech recognition, translation, sentiment analysis, and keyword extraction rather than using a single model?
RQ4
How can commercial speech-recognition APIs and open-source models such as Whisper be systematically benchmarked for regional-language interview processing?
RQ5
How accurately does the pipeline preserve semantic meaning during translation and downstream analysis?
RQ6
How can AI output be evaluated according to its usefulness for qualitative research rather than transcription accuracy alone?
________________________________________
4. Main Contributions
The main contributions of this study are:
1.	A complete multilingual speech-to-insight pipeline for long-duration Bengali interviews.
2.	A practical long-audio processing strategy that segments recordings into manageable units before ASR.
3.	A model-specialization approach in which different AI models are selected for different tasks.
4.	A Bengali agricultural interview case study containing realistic domain-specific vocabulary and code-mixed expressions.
5.	A benchmarking framework for comparing commercial APIs and open-source ASR models.
6.	A Research Utility Score (RUS) that extends conventional ASR evaluation beyond WER/CER.
7.	A traceable research workflow connecting transcript, translation, extracted themes, and evidence.
________________________________________
5. Proposed Pipeline
The proposed system consists of the following stages:
Long Bengali Interview Audio
              │
              ▼
      Audio Pre-processing
              │
              ▼
      Long-Audio Segmentation
              │
              ▼
       ┌───────────────┐
       │   ASR Models  │
       │ Sarvam /      │
       │ Whisper /     │
       │ Other Models  │
       └───────────────┘
              │
              ▼
       Bengali Transcript
              │
              ▼
      Sentence Segmentation
              │
              ▼
     Bengali → English
        Translation
              │
              ▼
     ┌───────────────────┐
     │ Downstream NLP    │
     ├───────────────────┤
     │ XLM-R Sentiment   │
     │ KeyBERT Keywords  │
     │ Theme Extraction  │
     └───────────────────┘
              │
              ▼
     Evidence-Linked Results
              │
              ▼
       Research Utility
          Evaluation
              │
              ▼
        Interactive View
The dashboard is therefore considered an output layer, rather than the primary contribution of the study.
The main contribution lies in the backend processing and evaluation pipeline.
________________________________________
6. Why Sarvam AI Was Selected for ASR
The choice of Sarvam AI was motivated by the target language and deployment requirements.
Sarvam's speech-to-text API explicitly supports Bengali through the bn-IN language code and provides support for multiple Indian languages.
This makes it particularly relevant for a study focused on Indian regional-language speech.
The experimental implementation used:
language_code = "bn-IN"
and sent each audio segment to the speech-to-text service.
Sarvam was therefore selected not simply because it produced a transcript, but because it represents a commercial/API-based Indian-language ASR approach suitable for comparison against open-source alternatives.
This distinction is important for the paper.
The study is not claiming that Sarvam is universally better than Whisper.
Instead, the framework establishes a method through which Sarvam, Whisper, and other ASR systems can be compared under the same Bengali interview conditions.
________________________________________
7. Open-Source vs Commercial ASR Benchmark
A major research direction of this work is the comparison between:
Commercial/API-based ASR
Sarvam AI
Advantages to investigate:
•	Indian-language specialization;
•	API accessibility;
•	deployment simplicity;
•	potentially lower local computational requirements.
Open-source ASR
Whisper
Advantages to investigate:
•	local execution;
•	model transparency;
•	no per-request API dependency;
•	multiple model sizes;
•	multilingual speech recognition.
Whisper has been trained on a large multilingual speech corpus, while research specifically investigating Indian languages has noted that low-resource Indian-language recognition can remain challenging and that prompting/tokenization strategies can affect performance.
The proposed benchmark should therefore compare the systems rather than assume that either approach is inherently superior.
________________________________________
8. Long-Audio Processing
The experimental recording lasted:
1,143.51 seconds ≈ 19.06 minutes
The system divided the recording into:
40 × approximately 29-second segments.
The segmentation strategy was implemented to remain below the API duration constraint used in the experiment.
Processing sequence
[
A \rightarrow {A_1,A_2,\ldots,A_{40}}
]
where each (A_i) is approximately 29 seconds.
Each segment was independently submitted for transcription:
[
A_i \rightarrow T_i
]
and the final transcript was constructed as:
[
T = T_1 \oplus T_2 \oplus ... \oplus T_{40}
]
where (\oplus) represents sequential transcript concatenation.
Context Problem
However, segmentation creates a second research challenge.
If a sentence begins at the end of one chunk and continues into the next, independent processing may lose contextual information.
This creates the possibility of:
•	sentence discontinuity;
•	repeated words;
•	missing words;
•	inconsistent punctuation;
•	semantic drift across chunk boundaries.
Therefore, future experiments should compare:
1.	non-overlapping chunks;
2.	overlapping chunks;
3.	sentence-aware segmentation;
4.	timestamp-based alignment.
This makes context preservation an explicit research variable rather than simply claiming that chunking solves the long-audio problem.
________________________________________
9. Bengali Linguistic Diversity
The experimental transcript demonstrates substantial Bengali-English mixing.
For example, the interview includes phrases related to:
•	climate change;
•	extreme heat;
•	weather;
•	water logging;
•	market crisis;
•	soil testing;
•	technical support;
•	AI;
•	IoT;
•	real-time testing.
This type of speech should be treated as code-mixed conversational Bengali, rather than assuming that all speech is pure Bengali.
This distinction matters because code-switching can affect:
•	language identification;
•	tokenization;
•	pronunciation modeling;
•	ASR vocabulary;
•	translation;
•	sentiment classification;
•	keyword extraction.
Recent multilingual NLP research continues to use XLM-RoBERTa specifically for multilingual and code-mixed sentiment settings, demonstrating the relevance of multilingual transformer representations to such problems.
________________________________________
10. Why Translation Is Used
The Bengali transcript is retained as the primary source representation.
However, the current downstream NLP pipeline operates on English translation.
The workflow is:
[
Bengali\ Transcript
\rightarrow
English\ Translation
\rightarrow
NLP
]
The implementation used GoogleTranslator to translate the sentence-level Bengali transcript into English.
This design was adopted because it enables the use of established English-compatible NLP models for sentiment and semantic keyword extraction.
However, translation should not be considered lossless.
Therefore, the proposed evaluation includes semantic fidelity as a separate metric.
________________________________________
11. Why XLM-RoBERTa Was Used for Sentiment Analysis
This point should be explicitly explained in the paper because Jeet specifically asked:
“What is XLM-RoBERTa? Is it directly analysing the sentiment from Bengali transcripts?”
Answer:
In the current implementation, no.
The system does not directly perform sentiment analysis on the original Bengali transcript.
The actual pipeline is:
[
Bengali\ Transcript
\rightarrow
English\ Translation
\rightarrow
XLM\text{-}RoBERTa
\rightarrow
Sentiment
]
The code confirms that the translated text is passed to the sentiment model.
XLM-RoBERTa is a multilingual Transformer-based language model trained on 100 languages. Its original research demonstrated strong cross-lingual performance and particularly strong improvements for low-resource languages.
The selected implementation uses:
cardiffnlp/twitter-xlm-roberta-base-sentiment
for sentiment classification.
The reason for selecting an XLM-R-based model is therefore its multilingual representation capability and suitability as a transformer-based text classifier.
Important limitation
Because the current pipeline translates Bengali into English before sentiment analysis, the final sentiment result reflects:
Bengali speech + ASR quality + translation quality + XLM-R classification
rather than XLM-R's direct understanding of the original Bengali transcript.
This is an important limitation and should be explicitly acknowledged.
________________________________________
12. Why KeyBERT Was Used for Keyword Extraction
Jeet referred to BERT for keyword extraction, and this should be explained precisely.
KeyBERT is a semantic keyword-extraction approach that uses BERT-style embeddings and cosine similarity to identify words or phrases most similar to the overall document representation.
The implementation uses:
KeyBERT
+
all-MiniLM-L6-v2
and extracts one- and two-word phrases.
Therefore, the architecture is:
[
English\ Interview
\rightarrow
Sentence\ Embeddings
\rightarrow
Candidate\ Keywords
\rightarrow
Cosine\ Similarity
\rightarrow
Ranked\ Keywords
]
The purpose is to identify the major concepts discussed in the interview rather than simply counting word frequency.
________________________________________
13. Experimental Dataset
The experimental dataset consists of a Bengali agricultural interview.
The interview addresses:
•	agricultural challenges;
•	climate change;
•	extreme weather;
•	water logging;
•	crop diseases;
•	soil health;
•	fertilizer usage;
•	soil testing;
•	technology adoption;
•	IoT;
•	market crisis;
•	farmer profitability.
The recording duration is:
1,143.51 seconds
and the system generated:
40 audio chunks.
The transcript was subsequently divided into sentence-level units, with the implementation reporting 123 sentence chunks.
________________________________________
14. Benchmarking Metrics
The proposed evaluation framework contains two levels.
14.1 ASR-Level Metrics
Word Error Rate
[
WER=\frac{S+D+I}{N}
]
where:
•	(S) = substitutions;
•	(D) = deletions;
•	(I) = insertions;
•	(N) = number of words in the reference transcript.
Character Error Rate
[
CER=\frac{S+D+I}{N}
]
calculated at the character level.
These metrics measure transcription quality.
________________________________________
15. Semantic Fidelity
Because translation is part of the proposed pipeline, ASR accuracy alone is insufficient.
Semantic fidelity measures whether the meaning of the Bengali statement remains consistent after translation.
Possible measures include:
•	human semantic-rating scores;
•	multilingual sentence-embedding similarity;
•	BERTScore;
•	expert annotation.
The study should report this independently from WER/CER.
________________________________________
16. Narrative Extraction
For qualitative research, the system must identify whether important themes have been preserved.
For the agricultural interview, possible themes include:
•	climate-related agricultural risks;
•	soil degradation;
•	fertilizer misuse;
•	soil testing;
•	technology adoption;
•	market instability.
The evaluation should compare automatically extracted themes against expert annotations.
________________________________________
17. Evidence Grounding
A major improvement over conventional NLP analysis is to make every extracted theme traceable to the original transcript.
For example:
Theme:
Soil Testing

Source:
Bengali transcript segment

Timestamp:
XX:XX–XX:XX

English Translation:
...

Evidence:
Original transcript sentence
This prevents the system from producing themes without supporting evidence.
________________________________________
18. Processing Efficiency
The framework should also measure:
•	total processing time;
•	ASR processing time;
•	translation time;
•	NLP processing time;
•	number of API requests;
•	API cost;
•	local computational requirements.
This is particularly important when comparing a cloud API with an open-source model.
A model with slightly better WER may not necessarily be the best choice if it requires significantly more computation or cost.
________________________________________
19. Research Reproducibility
Repeated runs should be evaluated to determine whether the same input produces consistent outputs.
For example:
[
R = 1-\frac{Variation}{Maximum\ Possible\ Variation}
]
can be used as a normalized reproducibility component.
The exact formulation can be finalized after defining the experimental protocol.
________________________________________
20. Research Utility Score
The central proposed evaluation metric is:
Research Utility Score (RUS)
The RUS extends conventional ASR benchmarking by measuring whether the complete AI output is useful for qualitative research.
The score contains six dimensions:
Dimension	What it measures
Transcription Quality	WER/CER
Semantic Fidelity	Meaning preservation
Narrative Extraction	Correct themes/adaptation strategies
Evidence Grounding	Traceability to transcript
Processing Efficiency	Runtime and cost
Reproducibility	Consistency across runs
A general formulation is:
[
RUS =
w_1TQ+
w_2SF+
w_3NE+
w_4EG+
w_5PE+
w_6RP
]
subject to:
[
\sum_{i=1}^{6}w_i=1
]
The weights should be determined experimentally or through expert consultation rather than arbitrarily assigned.
The important contribution is therefore not simply proposing another accuracy metric, but changing the evaluation question from:
“Did the model transcribe the words correctly?”
to:
“Did the system produce reliable, meaningful, traceable, and reproducible information for research?”
________________________________________
21. Results
The implemented system processed the complete interview through the proposed pipeline.
Audio Processing
Parameter	Result
Audio duration	1,143.51 seconds
Approximate duration	19.06 minutes
Chunk duration	29 seconds
Number of chunks	40
Sentence chunks	123
NLP Output
Component	Result
ASR language	Bengali
Translation	Bengali → English
Sentiment model	XLM-RoBERTa
Sentiment	Negative
Sentiment confidence	41.7%
Keyword model	KeyBERT
Keywords	10
The current project does not contain a manually verified reference transcript, so WER/CER should not yet be reported as experimental results.
Similarly, a numerical RUS should not be claimed until the additional annotation and benchmarking experiments are performed.
________________________________________
22. Discussion
The results demonstrate that a long Bengali agricultural interview can be processed through a multi-stage AI pipeline consisting of speech recognition, translation, sentiment analysis, and semantic keyword extraction.
The main research observation is that model specialization is preferable to assuming that one model can optimally perform every task.
Sarvam AI serves the speech-recognition stage because the target problem involves Indian regional-language audio.
XLM-RoBERTa serves the multilingual text-classification stage because it was designed for cross-lingual representation learning across many languages.
KeyBERT serves semantic keyword extraction because it ranks candidate phrases based on embedding similarity rather than simple frequency.
This modular design allows individual components to be replaced without redesigning the entire pipeline.
For example:
[
Sarvam\ ASR
\rightarrow Whisper
]
can be tested without changing the sentiment or keyword modules.
Likewise:
[
XLM-R
\rightarrow Bengali\text{-}specific\ model
]
can be evaluated independently.
This makes the framework useful as a benchmarking architecture, rather than simply a single implementation.
________________________________________
23. Limitations
The current study has several limitations.
23.1 Single Interview
The current experiment uses one agricultural interview and therefore cannot establish general performance across Bengali speakers or domains.
23.2 No Ground-Truth Transcript
A manually corrected reference transcript is required for WER/CER evaluation.
23.3 Translation-Based Sentiment Analysis
The sentiment model does not currently analyze the Bengali transcript directly. It analyzes the English translation.
23.4 Chunk Boundary Effects
Independent 29-second segments may introduce context loss at boundaries.
23.5 Model Comparison Not Yet Completed
The current implementation establishes the Sarvam-based pipeline, but a scientifically valid Sarvam-vs-Whisper comparison requires running both systems on the same audio and evaluating them against the same reference transcript.
23.6 Keyword Quality
Some automatically generated keyword phrases are semantically relevant but grammatically awkward. The extracted results include phrases such as “agriculture reduce” and “terms agriculture.”
________________________________________
24. Future Work
The next phase of the research should focus on the following experiments.
Experiment 1 — ASR Benchmark
Compare:
•	Sarvam AI;
•	Whisper Small;
•	Whisper Medium;
•	Whisper Large;
•	potentially other Indian-language ASR systems.
Experiment 2 — Bengali vs Code-Mixed Speech
Create subsets containing:
•	pure Bengali;
•	Bengali-English;
•	Bengali-Hindi-English;
•	technical agricultural terminology.
Experiment 3 — Long-Audio Strategies
Compare:
•	29-second chunks;
•	overlapping chunks;
•	longer chunks where supported;
•	sentence-aware segmentation.
Experiment 4 — Translation Evaluation
Measure semantic preservation between:
Bengali reference → English translation
and human-validated translations.
Experiment 5 — Sentiment Evaluation
Compare:
•	translated-English XLM-R;
•	direct Bengali-capable sentiment models;
•	multilingual models;
•	human annotations.
Experiment 6 — Research Utility Score
Calculate RUS using multiple annotated interviews.
________________________________________
25. Conclusion
This study proposes a multilingual speech-to-insight framework for processing long-duration Bengali interviews and evaluating the resulting AI outputs according to their usefulness for qualitative research.
Unlike systems that focus exclusively on transcription or visualization, the proposed framework treats the complete backend pipeline as the primary research object. The architecture combines specialized models for speech recognition, translation, sentiment analysis, and semantic keyword extraction.
Sarvam AI was selected as the experimental ASR platform because of its explicit support for Bengali and other Indian languages, while XLM-RoBERTa was selected for multilingual sentiment analysis and KeyBERT for semantic keyword extraction.
The experimental recording contained approximately 19 minutes of Bengali agricultural speech and was processed as 40 approximately 29-second audio segments.
The system successfully generated a Bengali transcript, English translation, sentiment classification, and semantic keyword list. However, the current experiment does not yet provide sufficient ground-truth data for claiming WER/CER performance or a numerical Research Utility Score.
The proposed RUS addresses this limitation conceptually by evaluating six dimensions: transcription quality, semantic fidelity, narrative extraction, evidence grounding, processing efficiency, and reproducibility.
The resulting framework therefore serves two purposes: first, it provides an implementable pipeline for analyzing Bengali interviews; second, it establishes a methodology for future researchers to compare commercial APIs and open-source ASR systems under realistic multilingual and long-duration conditions.
The broader research objective is not to identify one universally superior AI model. Instead, it is to determine which combination of models and processing strategies provides the most reliable and useful research output for multilingual qualitative interview analysis.
