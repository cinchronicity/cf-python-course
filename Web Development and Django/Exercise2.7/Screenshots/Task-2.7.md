# Task 2.7:

## Search Criteria and User Needs Analysis

### What Users Should Be Able to Search For:

1. **Recipe Name** - Primary search field

   - Full or partial recipe names
   - Example: "Chicken" should return "Chicken Parmesan", "Chicken Curry", etc.

2. **Ingredients** - Search by ingredient names

   - Users can find recipes containing specific ingredients
   - Example: "tomato" returns recipes with tomatoes

3. **Category** - Filter by meal type

   - Breakfast, Lunch, Dinner, Dessert, etc.
   - Dropdown selection for better UX

4. **Difficulty Level** - Filter by cooking complexity

   - Easy, Medium, Hard
   - Helps users find recipes matching their skill level

5. **Cooking Time Range** - Filter by time constraints

   - Quick meals (< 30 min), Standard (30-60 min), Long cooking (60+ min)
   - Useful for busy schedules

6. **Number of Servings** - Filter by portion size
   - Individual (1-2), Family (3-6), Large group (6+)
   - Helps with meal planning

### Search Input Format:

**Form Fields:**

- **Recipe Name**: Text input with autocomplete suggestions
- **Ingredients**: Text input (comma-separated or single ingredient)
- **Category**: Dropdown selection with "All Categories" option
- **Difficulty**: Checkbox or radio buttons (Easy/Medium/Hard)
- **Max Cooking Time**: Slider or number input (in minutes)
- **Servings**: Number range input
- **Search Button** and **Show All** button

### Output Format and Display:

**Search Results Table Columns:**

1. Recipe Image (thumbnail)
2. Recipe Name (clickable link to detail page)
3. Category
4. Difficulty Level (with visual indicators)
5. Total Time
6. Servings
7. Brief Description (truncated)
8. Actions (View Recipe, Add to Favorites if logged in)

**Table Features:**

- Sortable columns for better navigation
- Pagination for large result sets
- Recipe count display ("Found 15 recipes")
- Clear search criteria display
- "Clear all filters" option

### User Experience Considerations:

**Search Behavior:**

- Partial matching enabled (wildcard search)
- Case-insensitive search
- Multiple criteria combined with AND logic
- Empty search shows all recipes (Show-All functionality)

**Results Display:**

- Results sorted by relevance/popularity
- Visual indicators for difficulty (color coding)
- Hover effects on clickable recipe names
- Responsive table design for mobile

**Error Handling:**

- No results found message with suggestions
- Invalid input handling
- Form validation with helpful error messages

### Technical Implementation Notes:

**Django QuerySet Filtering:**

- Use `icontains` for partial text matching
- Combine multiple Q objects for complex searches
- Optimize queries with `select_related` for foreign keys

**Pandas DataFrame Conversion:**

- Convert QuerySet to DataFrame for table display
- Handle image URLs and foreign key relationships
- Format data for clean table presentation

**Performance Considerations:**

- Add database indexes on searchable fields
- Implement pagination for large datasets
- Consider search result caching for popular queries

### Bonus Features to Implement:

1. **Wildcard Search**:

   - "chick\*" matches "Chicken Parmesan"
   - "\*cake" matches "Chocolate Cake"
   - "c\*ke" matches "Cupcake"

2. **Search History**: Save user's recent searches
3. **Search Suggestions**: Auto-complete for recipe names
4. **Advanced Filters**: Dietary restrictions, prep time separate from cook time
5. **Save Search**: Allow users to bookmark search criteria

## Data Analysis

### Chart Implementation Plan for "Saved Recipes" Page

I decided to enhance the user's personal "Saved" page (renamed from "My Favorites") with three meaningful data visualizations that provide personalized cooking insights and practical value.

### Chart 1: Bar Chart - "Your Most Saved Ingredients"

- **Purpose**: Help users identify ingredients they should stock up on based on their saved recipe preferences
- **X-Axis**: Ingredient names (e.g., "Chicken", "Tomato", "Garlic", "Olive Oil")
- **Y-Axis**: Frequency count (number of saved recipes containing each ingredient)
- **Labels**:
  - Title: "Most Common Ingredients in Your Saved Recipes"
  - X-Axis Label: "Ingredients"
  - Y-Axis Label: "Number of Saved Recipes"
- **Display Logic**: Shown automatically when user has saved recipes, top 10 most frequent ingredients
- **User Value**: Grocery planning, pantry stocking decisions

### Chart 2: Pie Chart - "Your Saved Recipe Categories"

- **Purpose**: Show user's cooking interests and preferences breakdown
- **Data**: Percentage distribution of saved recipes by category
- **Labels**:
  - Title: "Your Recipe Preferences by Category"
  - Segments: Category names with percentages (e.g., "Dinner 45%", "Dessert 25%")
- **Display Logic**: Shown automatically when user has saved recipes
- **User Value**: Self-awareness of cooking patterns, meal planning balance

### Chart 3: Line Chart - "Cooking Time Preferences"

- **Purpose**: Reveal whether user prefers quick meals vs elaborate cooking projects
- **X-Axis**: Cooking time ranges ("0-15 min", "16-30 min", "31-60 min", "60+ min")
- **Y-Axis**: Number of saved recipes in each time range
- **Labels**:
  - Title: "Your Saved Recipes by Cooking Time"
  - X-Axis Label: "Total Cooking Time (minutes)"
  - Y-Axis Label: "Number of Saved Recipes"
- **Display Logic**: Shown automatically when user has saved recipes
- **User Value**: Understanding time commitments, finding recipes that match available time

## Execution flow

### Key Navigation Features:

**1. Homepage Features:**

- Featured recipe display
- Site statistics (total recipes, users, favorites)
- Navigation to all main sections

**2. Recipe Search Features:**

- Advanced search with multiple criteria
- Real-time filtering by difficulty, time, servings
- Results displayed in organized table format
- Direct access to recipe details

**3. Authentication Features:**

- Secure login/logout flow
- Protected favorites functionality
- Personalized experience for logged-in users

**4. Favorites System:**

- Save/unsave recipes (login required)
- View cooking insights with charts
- Personal recipe collection management

**5. Recipe Management:**

- Detailed recipe information
- Difficulty calculation (Easy/Medium/Hard)
- Ingredient lists and cooking instructions
- Category-based organization

### Example User Journey:

```
User lands on Homepage
    ↓
Sees featured recipe "Garlic Pasta"
    ↓
Clicks "Search Recipes"
    ↓
Searches for "difficulty: Easy" recipes
    ↓
Views search results in table format
    ↓
Clicks on "Quick Toast" recipe
    ↓
Views recipe details (5 min cook time, 2 ingredients)
    ↓
Wants to save recipe → Prompted to login
    ↓
Logs in with credentials
    ↓
Redirected back to recipe → Clicks "Save Recipe"
    ↓
Goes to "Saved Recipes" page
    ↓
Views cooking insights charts
    ↓
Sees recipe difficulty distribution
    ↓
Continues browsing or logs out
```

This flow demonstrates the complete user experience from discovery to engagement, showcasing all the key features implemented in the recipe application.
