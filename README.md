# Food RAG

This is a Retrieval-Augmented Generation (RAG) system that uses Gemini 2.0 Flash as an LLM. It leverages a subset of the [EpiRecipes dataset](https://www.kaggle.com/datasets/hugodarwood/epirecipes) from Kaggle and employs Qdrant for vector storage.

## Data Preparation


The dataset was processed in a Kaggle notebook to extract a relevant subset. Additionally, ingredient quantity units were missing in the original dataset, so they were scraped from external sources. These processed data points were then uploaded to Supabase, where three tables were created:
  1. units - Contains ingredient quantity units.

  2. foodcom - Stores the main recipe information.

  3. food - A final joined table combining units and foodcom.

**Database Schema in Supabase**


```sql
CREATE TABLE units (
  RecipeId SMALLINT,
  Units TEXT
);

CREATE TABLE foodcom (
  id SERIAL PRIMARY KEY,
  RecipeId SMALLINT,
  Name TEXT,
  RecipeIngredientQuantities TEXT,
  RecipeIngredientParts TEXT,
  Calories FLOAT4,
  FatContent FLOAT4,
  CarbohydrateContent FLOAT4,
  FiberContent FLOAT4,
  ProteinContent FLOAT4,
  RecipeInstructions TEXT
);

CREATE TABLE food (
  id SERIAL PRIMARY KEY,
  RecipeId SMALLINT,
  Name TEXT,
  RecipeIngredientQuantities TEXT,
  Units TEXT,
  RecipeIngredientParts TEXT,
  Calories FLOAT4,
  FatContent FLOAT4,
  CarbohydrateContent FLOAT4,
  FiberContent FLOAT4,
  ProteinContent FLOAT4,
  RecipeInstructions TEXT
);

INSERT INTO food (RecipeId, Name, RecipeIngredientQuantities, Units, RecipeIngredientParts, Calories, FatContent, CarbohydrateContent, FiberContent, ProteinContent, RecipeInstructions)
SELECT foodcom.RecipeId, foodcom.Name, foodcom.RecipeIngredientQuantities, units.Units, foodcom.RecipeIngredientParts, foodcom.Calories, foodcom.FatContent, foodcom.CarbohydrateContent, foodcom.FiberContent, foodcom.ProteinContent, foodcom.RecipeInstructions
FROM foodcom
JOIN units ON foodcom.RecipeId = units.RecipeId;
```

3. **Export and Processing**
   The `food` table was downloaded as a CSV file (`food_rows.csv`) since Supabase free-tier projects may be deleted over time.
   The CSV file was converted into a Pandas DataFrame in Jupyter Notebook. Basic data cleaning steps included:

    - Using .describe() to inspect statistical values.

    - Checking for null values (none found).

    - Checking for duplicate rows (none found).

## RAG System Implementation

- **Qdrant** was chosen as the vector database due to its support for `":memory:"`, allowing for fast, in-memory indexing and retrieval, making it ideal for quick demos.
- **Gemini 2.0 Flash** was used as the LLM to process user queries.
- The system takes a user prompt and retrieves relevant recipes based on the embeddings stored in Qdrant.

## Usage

- Run the Jupyter notebook to interact with the RAG system.
- Feel free to swap Gemini for another LLM if needed.
- Remember to set your Gemini API key as a secret before running the notebook.

## Future Improvements

- Explore deploying the system with persistent storage instead of `":memory:"`.
- Experiment with fine-tuning LLM responses based on user preferences.
- Integrate additional filtering (e.g., dietary preferences, allergens).




