# Noisy Student Training to identify Textual Elements in Unsupervised News Data via Argumentative Essay Pieces

BY **Liew Wei Pyn and Prannaya Gupta**

Done for the **CS5131** Introduction to Artificial Intelligence Final Project

<hr>

To access models, access `model_url.txt` and use the Google Drive Link. Follow `README.docx` to access the large model files. Follow `development/README.md` to learn how to load the UI.



<hr>

## Proposal

**Domain**: Literature, Education, English

**Subject Area**: Natural Language Processing, Deep Neural Network, BERT, Transformers, Transfer Learning, Sequential Sentence Classification

### Description

Argumentative Essays usually include a plethora of different essay elements that are quite  difficult for the average student to identify. These include, but are not strictly limited to, Lead, Position, Claim, Counterclaim, Rebuttal, Evidence,  Concluding Statement.

For instance, given a passage such as the  following: 

>  *Although the  history of human invention spans over millennia, there have been relatively  few game-changing technologies. From the manipulation of fire back in the primal age to the invention of the electronic transistor in the 1940s, these monumental developments have often been followed up by fervent exploration and a burgeoning of new technologies that stem from that initial spark.*

Here, you can state that this paragraph is the Lede, or the **Lead**. It is the  statement of facts prior to a statement of opinion, and this is a very objective set of statements. 

However, after this, the author writes the  following: 

> *While some  may say Artificial Intelligence, or AI, is akin to these other inventions, I  beg to disagree.*  

This is a **Position**,  as can be said from the subjective statement of opinion, which has yet to be  substantiated by fact or evidence. However, in a different context, this can  be classified as a **Rebuttal**  as well, since it started by giving an alternate perspective and then  admitting that this is not something that matches up with the perspective of  the author.

This contradiction can often cause confusion in  modern machine learning models, since they may classify sentences without  keeping track of context. Context is quite important in Natural Language  Processing (NLP) Tasks, which is something many models would not excel at.

Often, students struggling with or generally writing essays use automated writing feedback tools, which, while numerous, each have their own limitations. Many of these feedback tools are unable to  identify writing structures in essays, or are at least very inaccurate in  their identification. Many of these tools are proprietary, with algorithms and feature claims that cannot be backed up independently, and more importantly, that are inaccessible to educators due to high costs.

In addition, automatically and consistently identifying and highlighting such elements,  that too amongst hundreds of scripts, can be a tedious task for teachers, who  may wish not to use these tools due to, in summary, their high levels of  inaccuracy, lacking features and high costs.

**Objective(s)**: Developing a model capable of analyzing essay elements in argumentative pieces

### Target Users

- Teachers aiming to help their students improve their writing
- Students aiming to improve their writing to prepare for the A Level GP and University  Preparation

### Project Plan and Timeline

| Timeline         | Project Plan                                                 |
| ---------------- | ------------------------------------------------------------ |
| 28-1st February  | Load and prepare dataset                                     |
| 2-20th February  | Try different Hugging Face supported models (GPT2, BERT etc.), and evaluate their performances |
| 20-28th February | Create a frontend GUI                                        |
| 1st March        | Mid-Way project review                                       |
| 2-20th March     | Buffer time, pray we don’t need it                           |
| 21-29th March    | Report and Presentation                                      |

### Resources and Tools Use

- PyTorch
- GPUs
- Google Colaboratory
- Hugging Face
- Fast.AI

### Target Outcome and Benefits

A model capable of analysing and identifying the key argumentative elements in an English essay. We can possibly test it on real-life samples like model essays from teachers at NUS High.

### References

- [Feedback Prize - Evaluating Student Writing (Kaggle Competition, Georgia State University)](https://www.kaggle.com/c/feedback-prize-2021/overview)
- Zaheer, M., Guruganesh, G., Dubey, A., Ainslie, J., Alberti, C., Ontanon, S., … Ahmed, A. (2021). Big Bird: Transformers for Longer Sequences. *arXiv [cs.LG]*. Opgehaal van http://arxiv.org/abs/2007.14062
- Cohan, A., Beltagy, I., King, D., Dalvi, B., & Weld, D. (2019). Pretrained Language Models for Sequential Sentence Classification. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*. https://arxiv.org/pdf/1909.04054.pdf
- Beltagy, I., Peters, M. E., & Cohan, A. (2020). Longformer: The Long-Document Transformer. *arXiv [cs.CL]*. Opgehaal van http://arxiv.org/abs/2004.05150
- Press, O., Smith, N. A., & Lewis, M. (2021). Shortformer: Better Language Modeling using Shorter Inputs. *arXiv [cs.CL]*. Opgehaal van http://arxiv.org/abs/2012.15832

