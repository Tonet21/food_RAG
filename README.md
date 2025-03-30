# food_RAG

before the Rag I will do some statistical analysis with pandas 

```sql
create table units (
  RecipeI smallint,
  Units text
);


create table foodcom (
  id serial primary key,
  RecipeId smallint,
  Name text,
  RecipeIngredientQuantities text,
  RecipeIngredientParts text,
  Calories float4,
  FatContent float4,
  CarbohydrateContent float4,
  FiberContent float4,
  ProteinContent float4,
  RecipeInstructions text
);

create table food (
  id serial primary key,
  RecipeId smallint,
  Name text,
  RecipeIngredientQuantities text,
  Units text,
  RecipeIngredientParts text,
  Calories float4,
  FatContent float4,
  CarbohydrateContent float4,
  FiberContent float4,
  ProteinContent float4,
  RecipeInstructions text) ;


insert into food (RecipeId, name, RecipeIngredientQuantities, units, RecipeIngredientParts, Calories, FatContent, CarbohydrateContent, FiberContent, proteinContent, RecipeInstructions)
SELECT foodcom.recipeid, foodcom.name, foodcom.RecipeIngredientQuantities, units.units, foodcom.RecipeIngredientParts, foodcom.Calories, foodcom.FatContent, foodcom.CarbohydrateContent, foodcom.FiberContent, foodcom.proteinContent, foodcom.RecipeInstructions
FROM foodcom
JOIN units ON foodcom.recipeid = units.recipeid;
```
