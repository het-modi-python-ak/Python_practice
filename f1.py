{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "da8ef4ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helo\n"
     ]
    }
   ],
   "source": [
    "print(\"helo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fa46e40c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>qid</th>\n",
       "      <th>qname</th>\n",
       "      <th>question</th>\n",
       "      <th>type</th>\n",
       "      <th>sub</th>\n",
       "      <th>sq_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>QID18</td>\n",
       "      <td>TechEndorse_1</td>\n",
       "      <td>What attracts you to a technology or causes yo...</td>\n",
       "      <td>RO</td>\n",
       "      <td>AI integration or AI Agent capabilities</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>QID18</td>\n",
       "      <td>TechEndorse_2</td>\n",
       "      <td>What attracts you to a technology or causes yo...</td>\n",
       "      <td>RO</td>\n",
       "      <td>Easy-to-use API</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>QID18</td>\n",
       "      <td>TechEndorse_3</td>\n",
       "      <td>What attracts you to a technology or causes yo...</td>\n",
       "      <td>RO</td>\n",
       "      <td>Robust and complete API</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>QID18</td>\n",
       "      <td>TechEndorse_4</td>\n",
       "      <td>What attracts you to a technology or causes yo...</td>\n",
       "      <td>RO</td>\n",
       "      <td>Customizable and manageable codebase</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>QID18</td>\n",
       "      <td>TechEndorse_5</td>\n",
       "      <td>What attracts you to a technology or causes yo...</td>\n",
       "      <td>RO</td>\n",
       "      <td>Reputation for quality</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>134</th>\n",
       "      <td>QID103</td>\n",
       "      <td>AIAgentObsWrite</td>\n",
       "      <td>Was the tool or tools for AI agent observabili...</td>\n",
       "      <td>TE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>135</th>\n",
       "      <td>QID92</td>\n",
       "      <td>AIAgentExternal</td>\n",
       "      <td>You indicated you use or develop AI agents as ...</td>\n",
       "      <td>MC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>136</th>\n",
       "      <td>QID104</td>\n",
       "      <td>AIAgentExtWrite</td>\n",
       "      <td>Was the out-of-the-box agents, copilots or ass...</td>\n",
       "      <td>TE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137</th>\n",
       "      <td>QID100</td>\n",
       "      <td>AIHuman</td>\n",
       "      <td>In the future, if AI can do most coding tasks,...</td>\n",
       "      <td>MC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>138</th>\n",
       "      <td>QID93</td>\n",
       "      <td>AIOpen</td>\n",
       "      <td>Looking ahead 3–5 years, what skills do you be...</td>\n",
       "      <td>TE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>139 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        qid            qname  \\\n",
       "0     QID18    TechEndorse_1   \n",
       "1     QID18    TechEndorse_2   \n",
       "2     QID18    TechEndorse_3   \n",
       "3     QID18    TechEndorse_4   \n",
       "4     QID18    TechEndorse_5   \n",
       "..      ...              ...   \n",
       "134  QID103  AIAgentObsWrite   \n",
       "135   QID92  AIAgentExternal   \n",
       "136  QID104  AIAgentExtWrite   \n",
       "137  QID100          AIHuman   \n",
       "138   QID93           AIOpen   \n",
       "\n",
       "                                              question type  \\\n",
       "0    What attracts you to a technology or causes yo...   RO   \n",
       "1    What attracts you to a technology or causes yo...   RO   \n",
       "2    What attracts you to a technology or causes yo...   RO   \n",
       "3    What attracts you to a technology or causes yo...   RO   \n",
       "4    What attracts you to a technology or causes yo...   RO   \n",
       "..                                                 ...  ...   \n",
       "134  Was the tool or tools for AI agent observabili...   TE   \n",
       "135  You indicated you use or develop AI agents as ...   MC   \n",
       "136  Was the out-of-the-box agents, copilots or ass...   TE   \n",
       "137  In the future, if AI can do most coding tasks,...   MC   \n",
       "138  Looking ahead 3–5 years, what skills do you be...   TE   \n",
       "\n",
       "                                         sub  sq_id  \n",
       "0    AI integration or AI Agent capabilities    1.0  \n",
       "1                            Easy-to-use API    2.0  \n",
       "2                    Robust and complete API    3.0  \n",
       "3       Customizable and manageable codebase    4.0  \n",
       "4                     Reputation for quality    5.0  \n",
       "..                                       ...    ...  \n",
       "134                                      NaN    NaN  \n",
       "135                                      NaN    NaN  \n",
       "136                                      NaN    NaN  \n",
       "137                                      NaN    NaN  \n",
       "138                                      NaN    NaN  \n",
       "\n",
       "[139 rows x 6 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('Data/survey_results_schema.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0f0bccb",
   "metadata": {},
   "source": [
    "Creating simple data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8421dea1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>raj</td>\n",
       "      <td>failed</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>raju</td>\n",
       "      <td>pass</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ramesh</td>\n",
       "      <td>failed</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>kanu</td>\n",
       "      <td>pass</td>\n",
       "      <td>hok</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name  stauts  age\n",
       "0  mahesh    pass    4\n",
       "1     raj  failed   54\n",
       "2    raju    pass   34\n",
       "3  ramesh  failed    3\n",
       "4    kanu    pass  hok"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "people = { \"name\" : [\"mahesh\",\"raj\",\"raju\",\"ramesh\",\"kanu\"],\n",
    "\"stauts\" : [\"pass\",\"failed\",\"pass\",\"failed\",\"pass\"],\n",
    "\"age\" : [4,54,34,3,\"hok\"]\n",
    "}\n",
    "\n",
    "dk = pd.DataFrame(people)\n",
    "dk"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70a493b6",
   "metadata": {},
   "source": [
    "type of the column returns the data type series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a3c588d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dk['age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e3056da0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.count of      name  stauts  age\n",
       "0  mahesh    pass    4\n",
       "1     raj  failed   54\n",
       "2    raju       p   34\n",
       "3  ramesh       f    3\n",
       "4    kanu    pass  hok>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "062a3fc4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>raj</td>\n",
       "      <td>failed</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name  stauts age\n",
       "0  mahesh    pass   4\n",
       "1     raj  failed  54"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.loc[[0,1]]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "78160ace",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>raj</td>\n",
       "      <td>failed</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name  stauts\n",
       "0  mahesh    pass\n",
       "1     raj  failed"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.iloc[[0,1],[0,1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "905d76e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "stauts\n",
       "pass      3\n",
       "failed    2\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk['stauts'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "70a8541e",
   "metadata": {},
   "outputs": [],
   "source": [
    "dk.set_index('age',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2eb59fbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>raju</td>\n",
       "      <td>pass</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name stauts age\n",
       "0  mahesh   pass   4\n",
       "2    raju   pass  34"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.loc[[0,2]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "7286bcd7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>age</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>raj</td>\n",
       "      <td>failed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>raju</td>\n",
       "      <td>pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ramesh</td>\n",
       "      <td>failed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hok</th>\n",
       "      <td>kanu</td>\n",
       "      <td>pass</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       name  stauts\n",
       "age                \n",
       "4    mahesh    pass\n",
       "54      raj  failed\n",
       "34     raju    pass\n",
       "3    ramesh  failed\n",
       "hok    kanu    pass"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "184ee51d",
   "metadata": {},
   "outputs": [],
   "source": [
    "fl = dk['age']==34"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "68b39da5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>stauts</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mahesh</td>\n",
       "      <td>pass</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>raj</td>\n",
       "      <td>failed</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ramesh</td>\n",
       "      <td>failed</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>kanu</td>\n",
       "      <td>pass</td>\n",
       "      <td>hok</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name  stauts  age\n",
       "0  mahesh    pass    4\n",
       "1     raj  failed   54\n",
       "3  ramesh  failed    3\n",
       "4    kanu    pass  hok"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dk.loc[~fl]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "416011bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name  Score\n",
      "1      Bob     90\n",
      "2  Charlie     78\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = {'Name': ['Alice', 'Bob', 'Charlie'],\n",
    "        'Age': [25, 32,45],\n",
    "        'Score': [85, 90, 78]}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Filter rows where Age > 30 and select only 'Name' and 'Score' columns\n",
    "filtered_df = df.loc[df['Age'] > 30, ['Name', 'Score']]\n",
    "print(filtered_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a3f330ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Name', 'Age', 'Score'], dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41d2591d",
   "metadata": {},
   "source": [
    "changing the column name "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a6ee6e70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>get otu</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>45</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   get otu  Age  Score\n",
       "0    Alice   25     85\n",
       "1      Bob   32     90\n",
       "2  Charlie   45     78"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.rename(columns={'Name':\"get otu\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bb652fd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_87835/1684179124.py:1: FutureWarning: Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. Value '30' has dtype incompatible with int64, please explicitly cast to a compatible dtype first.\n",
      "  df.loc[2] = ['jack','30','77']\n",
      "/tmp/ipykernel_87835/1684179124.py:1: FutureWarning: Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. Value '77' has dtype incompatible with int64, please explicitly cast to a compatible dtype first.\n",
      "  df.loc[2] = ['jack','30','77']\n"
     ]
    }
   ],
   "source": [
    "df.loc[2] = ['jack','30','77']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6795cc0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>jack</td>\n",
       "      <td>30</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Name Age Score\n",
       "0  Alice  25    85\n",
       "1    Bob  32    90\n",
       "2   jack  30    77"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26c441fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def chg(name):\n",
    "        \n",
    "    return name.upper()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ee075ccd",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[2,'Age']=50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0c618bb3",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'method' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdrop\u001b[49m\u001b[43m[\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m0,Age\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'method' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "df.drop[('0,Age')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "efb0ac2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Name', 'Age', 'Score'], dtype='object')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "afe49dc6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf\u001b[49m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "81f43682",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fu(x):\n",
    "    return str.x.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cd7eb366",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score\n",
       "0    alice   25     85\n",
       "1      bob   32     90\n",
       "2  charlie   50     78"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Name'] = df['Name'].apply(lambda x: x.lower())\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "318167b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score\n",
       "0    alice   25     85\n",
       "1      bob   32     90\n",
       "2  charlie   50     78"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "ca925f02",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['greet'] = df['Name']+ \" \" + \"hi\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "39cd5c9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "      <th>gree</th>\n",
       "      <th>greet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "      <td>alice hi</td>\n",
       "      <td>alice hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "      <td>bob hi</td>\n",
       "      <td>bob hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "      <td>charlie hi</td>\n",
       "      <td>charlie hi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score        gree       greet\n",
       "0    alice   25     85    alice hi    alice hi\n",
       "1      bob   32     90      bob hi      bob hi\n",
       "2  charlie   50     78  charlie hi  charlie hi"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "02ea1182",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "      <th>greet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "      <td>alice hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "      <td>bob hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "      <td>charlie hi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score       greet\n",
       "0    alice   25     85    alice hi\n",
       "1      bob   32     90      bob hi\n",
       "2  charlie   50     78  charlie hi"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(columns=\"gree\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "93d47c2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "      <th>gree</th>\n",
       "      <th>greet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "      <td>alice hi</td>\n",
       "      <td>alice hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "      <td>bob hi</td>\n",
       "      <td>bob hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "      <td>charlie hi</td>\n",
       "      <td>charlie hi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score        gree       greet\n",
       "0    alice   25     85    alice hi    alice hi\n",
       "1      bob   32     90      bob hi      bob hi\n",
       "2  charlie   50     78  charlie hi  charlie hi"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ad08d21f",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'DataFrame' object has no attribute 'append'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_42807/1664800846.py\u001b[0m in \u001b[0;36m?\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m'Name'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m'Raj'\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m?\u001b[0;34m(self, name)\u001b[0m\n\u001b[1;32m   6317\u001b[0m             \u001b[0;32mand\u001b[0m \u001b[0mname\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_accessors\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6318\u001b[0m             \u001b[0;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_info_axis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_can_hold_identifiers_and_holds_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6319\u001b[0m         ):\n\u001b[1;32m   6320\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 6321\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'DataFrame' object has no attribute 'append'"
     ]
    }
   ],
   "source": [
    "df.append({'Name':'Raj'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "342a8d69",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "cannot do slice indexing on RangeIndex with these indexers [Age] of type str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[38], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m df\u001b[38;5;241m.\u001b[39mloc[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m=\u001b[39m\u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mAge\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m:\u001b[49m\u001b[38;5;241;43m32\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/frame.py:4096\u001b[0m, in \u001b[0;36mDataFrame.__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   4094\u001b[0m \u001b[38;5;66;03m# Do we have a slicer (on rows)?\u001b[39;00m\n\u001b[1;32m   4095\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, \u001b[38;5;28mslice\u001b[39m):\n\u001b[0;32m-> 4096\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_getitem_slice\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   4098\u001b[0m \u001b[38;5;66;03m# Do we have a (boolean) DataFrame?\u001b[39;00m\n\u001b[1;32m   4099\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, DataFrame):\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/generic.py:4371\u001b[0m, in \u001b[0;36mNDFrame._getitem_slice\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   4366\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m   4367\u001b[0m \u001b[38;5;124;03m__getitem__ for the case where the key is a slice object.\u001b[39;00m\n\u001b[1;32m   4368\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m   4369\u001b[0m \u001b[38;5;66;03m# _convert_slice_indexer to determine if this slice is positional\u001b[39;00m\n\u001b[1;32m   4370\u001b[0m \u001b[38;5;66;03m#  or label based, and if the latter, convert to positional\u001b[39;00m\n\u001b[0;32m-> 4371\u001b[0m slobj \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mindex\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_convert_slice_indexer\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkind\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mgetitem\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m   4372\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(slobj, np\u001b[38;5;241m.\u001b[39mndarray):\n\u001b[1;32m   4373\u001b[0m     \u001b[38;5;66;03m# reachable with DatetimeIndex\u001b[39;00m\n\u001b[1;32m   4374\u001b[0m     indexer \u001b[38;5;241m=\u001b[39m lib\u001b[38;5;241m.\u001b[39mmaybe_indices_to_slice(\n\u001b[1;32m   4375\u001b[0m         slobj\u001b[38;5;241m.\u001b[39mastype(np\u001b[38;5;241m.\u001b[39mintp, copy\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m), \u001b[38;5;28mlen\u001b[39m(\u001b[38;5;28mself\u001b[39m)\n\u001b[1;32m   4376\u001b[0m     )\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/indexes/base.py:4255\u001b[0m, in \u001b[0;36mIndex._convert_slice_indexer\u001b[0;34m(self, key, kind)\u001b[0m\n\u001b[1;32m   4252\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m key\n\u001b[1;32m   4253\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdtype\u001b[38;5;241m.\u001b[39mkind \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124miu\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m   4254\u001b[0m     \u001b[38;5;66;03m# Note: these checks are redundant if we know is_index_slice\u001b[39;00m\n\u001b[0;32m-> 4255\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_validate_indexer\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mslice\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkey\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstart\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mgetitem\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m   4256\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_indexer(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mslice\u001b[39m\u001b[38;5;124m\"\u001b[39m, key\u001b[38;5;241m.\u001b[39mstop, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgetitem\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m   4257\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_indexer(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mslice\u001b[39m\u001b[38;5;124m\"\u001b[39m, key\u001b[38;5;241m.\u001b[39mstep, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgetitem\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/indexes/base.py:6752\u001b[0m, in \u001b[0;36mIndex._validate_indexer\u001b[0;34m(self, form, key, kind)\u001b[0m\n\u001b[1;32m   6747\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m   6748\u001b[0m \u001b[38;5;124;03mIf we are positional indexer, validate that we have appropriate\u001b[39;00m\n\u001b[1;32m   6749\u001b[0m \u001b[38;5;124;03mtyped bounds must be an integer.\u001b[39;00m\n\u001b[1;32m   6750\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m   6751\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m lib\u001b[38;5;241m.\u001b[39mis_int_or_none(key):\n\u001b[0;32m-> 6752\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_raise_invalid_indexer\u001b[49m\u001b[43m(\u001b[49m\u001b[43mform\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/indexes/base.py:4308\u001b[0m, in \u001b[0;36mIndex._raise_invalid_indexer\u001b[0;34m(self, form, key, reraise)\u001b[0m\n\u001b[1;32m   4306\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m reraise \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m lib\u001b[38;5;241m.\u001b[39mno_default:\n\u001b[1;32m   4307\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mreraise\u001b[39;00m\n\u001b[0;32m-> 4308\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(msg)\n",
      "\u001b[0;31mTypeError\u001b[0m: cannot do slice indexing on RangeIndex with these indexers [Age] of type str"
     ]
    }
   ],
   "source": [
    "df.loc[0]=df['Age':32]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "36625181",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Score</th>\n",
       "      <th>gree</th>\n",
       "      <th>greet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>charlie</td>\n",
       "      <td>50</td>\n",
       "      <td>78</td>\n",
       "      <td>charlie hi</td>\n",
       "      <td>charlie hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>bob</td>\n",
       "      <td>32</td>\n",
       "      <td>90</td>\n",
       "      <td>bob hi</td>\n",
       "      <td>bob hi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>alice</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "      <td>alice hi</td>\n",
       "      <td>alice hi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Age  Score        gree       greet\n",
       "2  charlie   50     78  charlie hi  charlie hi\n",
       "1      bob   32     90      bob hi      bob hi\n",
       "0    alice   25     85    alice hi    alice hi"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('Name',ascending=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
