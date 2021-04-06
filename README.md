## kiker_valet_solution
# Health AI Assistant by 'Кікер Валет' team
Contains solution of NLP task as part of a March.AI Hackathon presented by DOC.ua

### _General Task_:
Participants needed to create a smart medical assistant based on artificial intelligence. It will be the only entry point for users on all health issues, as well as simplify their interaction with medicine. The final product shoulded be in the form of a chatbot.
What a smart assistant shoulded be able to:
1) identify the disease by a set of symptoms;
2) advise the necessary tests for certain symptoms;
3) to determine the doctor to whom it is necessary to address on symptoms;
4) remind about taking pills;

#### 1. _Our model deals with illness-symptom-specialist database and data of previous patient's messages._
It is  preprocessing data:
- cleans textual data 
- lemmatizes text
- gets key word from message 

#### 2. _Also new data mined from open source for recommending medical analysis_

#### 3. _Model searches the database for occurrences of symptoms for a disease prediction and specialist recommendation. From here analysis recommendations becomes easier._
#### 4. _Telegram chatbot reminds about taking pills_

# screenshots of chatbot working

| Pills reminder             |  Start |  Doctor advisor | 
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/halynavs/kiker_valet_solution/blob/main/screenshots/pills-reminder.jpg)  |  ![](https://github.com/halynavs/kiker_valet_solution/blob/main/screenshots/start.jpg)|  ![](https://github.com/halynavs/kiker_valet_solution/blob/main/screenshots/doctor-advisor.jpg)



Task had some extra sup-tasks that wasn't covered in model in given 2 days of Hackathon duration:

5) find the right doctor, make an appointment at a convenient time or call him home;
6) find the right medicine and order delivery;
7) help to decipher the results of analyzes;
8) monitor basic health metrics and give advice on activities.

*A dataset with a license provided for use exclusively within the Hackathon, to solve the task. 


