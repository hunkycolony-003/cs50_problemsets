# Recipe Book
## Video Demo:
[Video link](https://youtu.be/GP5WRtkwKTI)
## Description:

HI, THIS IS CS50x FINAL POJECT.

## Files in the project:
This is a recipe book to store, view or edit your recipes. Here is used *.csv* files (as the recipe books) to store the data (recipes). The program was originally divided into two separate files one being `project.py` and `recipes.py`. In addition to a couple of more files `get_input.py` and `get_time.py` for some specific tasks throughout the program, which are explained later. But to meet the requirements of the project, `project.py` and `recipes.py` are merged into a single file, (`project.py`). A _.csv_ file is also included to test the file eith `test_project.py`.
## Details of the functionality:
#### Structure of a Book:
- User can create new books to catagorise their recipes. Each book can contain multiple recipes
- Name contains the name of the recipe. Servings contains the number of persons the recipe yield. Ingridient containts the desirable number of ingridients in the recipe.
- Each ingridient has two properties: `Name` and `Quantity`. `Quantity` has a value and an optional `unit`.
#### User Interface Elements:
- User is first welcomed with a `welcome message`.
- Then they are prompted for the _Book name_ (new/existing).
- Then they have four choices: `1. Add 2. View 3. Edit 4. Close`[^1] [^2].

[^1]: If an non-existent _Book name_ is given, the only option available are `Add` and `Close`. Any other input will result in reprompting the choice from the user.

[^2]: Any other input will result in reprompt.

##### Add:
- To add means to add a new recipe to a new or an existing recipe book.
- User are propted for a recipe __name__[^3] (a _str_), __servings__ (an _int_), and one or more __ingridients__.

[^3]: when adding recipe to an existing book, if a recipe with the same name already exists in the book, they will not further be prompted for the recipe and taken back to the input section.

- User will be prompted for _ingridient name_ and _ingridient quantity_[^4] (for the servings earlier mentioned) of each ingridient of the recipe and it will be repeated until the user types _done_ or uses _KeyboardInterruptKey_.

[^4]: Ingrient quantity comprises of a _int_ value, followed by a optional _str_ unit, with a space in-between.
- Then the recipe is added to the mentioned book.

##### View:

- This is to be used to view an already existing recipe.
- User is asked to enter the name(s) of the `recipe`(s) thet they want to view.[^5] [^6]
- Then they are asked to enter an _int_ as the number of `servings` that they want to view the `recipe`(s) for.
- The asked recipes will be showed to them to the user in a _table_ format,
- The quantites of the ingridients of the recipe(s) sre factored to the number of servings that they actually want to view the recipe for, rather than the `sevings` that the recipe was originaly written for.

[^5] Any name not present in the given `book`, will not be included in the table and others will be shown.

[^6] If they want to view every recipe in the book, they are need to enter ***all***.

##### Edit:

- This option is used to edit an existing _Book_.
- First of all, the user is given a list of the recipes present in the book.
- They can opt to edit the whole book or any one recipe.
- If opted for _whole_ the book is cleaned up and they are prompted to add a recipe.
- If a specific recipe choosen, and the recipe is present in the book, user is asked whether to _remove_ or _edit_ the recipe.[^7]
- Choosing _remove_ will remove the recipe from the book
- If _edit_ is chosen, the user is asked which property of the recipe that want to edit (between `name`, `servings`, `ingedients`). Also they can choose `whole`, in which case, they would be needed to re-write a whole recipe again.
- In case of `name` or `servings`, they are prompted for new values for the same and the recipe is updated. [^8]
- In case of `ingredients`, user is prompted whether they want to _add_ an _ingredient_ or _modify_ an existing one.
- If _edit_ is selected, the user is prompted for the _list_ of ingredients that they want to _modfy_.
- For every _ingredient_ present in the list, provided the _ingredient_ is present in the recipe, user is asked whether to _remove_ or _edit_ the _ingridient_. [^9]
- If _remove_ chosen, the recipe is rempved.
- If _edit_ is chosen, a new `ingredient` is prompted and added in place of the current _ingredient_.

[^7]: If recipe is not present, they will be escorted to the inpur section with an error message.

[^8]: If the new name already exists in the recipe, they will be taken back to the input section, with an error message.

[^9]: If the _ingredient_ is not present in the give `recipe`, am error message is shown.

##### Close:

- `Close` exits the program with an `Goodbye message`, which includes the current time of the day.
