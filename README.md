# Eat to Fit

Eat to Fit is a comprehensive web application designed to help users achieve their fitness and nutrition goals. The platform offers personalized nutrition plans, workout routines, and progress tracking to ensure users stay on track and reach their goals. Based on the recommendations from the web, the user can create their own meal plan and workout plan.

## Demonstration
[Watch my YouTube video](https://youtu.be/P9QOJjMesbU)

## Distinctiveness and Complexity

### Distinctiveness
Unlike typical fitness apps that focus solely on workout routines or nutrition apps that only track food intake, Eat to Fit integrates both aspects to provide a holistic approach to health and wellness. This integration allows users to see the correlation between their diet and exercise. Much different than an e-commerce, mail or search engine web application, this application actually takes into the user's biometric information and makes use of them to generate a nutrition plan and workout plan that fit the user's goal. 

### Complexity
The project demonstrates complexity through its various features and functionalities:
- **User Authentication**: Users can register, log in, and manage/modify their profiles.
- **Nutrition Plans**: Users can select meal plans, then receive a calculated daily nutritional intake, and log their food consumption.
- **Workout Routines**: Users can view recommended exercises, and add/remove their own exercises.
- **AJAX Integration**: The application uses AJAX for seamless form submissions and updates without reloading the page.
- **CSS and JavaScript Use**: The application uses CSS for a decent UX/UI and JavaScript to dynamically remove/add element on the web page.
- **Responsive Navigation Bar**: The navigation bar is desined in a way that if the user uses the application on a mobile device, they can navigate using the navigation bar.
## File Descriptions

### Models
- **models.py**: Defines the database models for UserProfile, NutritionPlan, FoodLog, WorkoutPlan, and UserLink.

### Forms
- **forms.py**: Contains the form classes for user registration, profile editing, nutrition plans, food logs, workout plans, and adding links.

### Views
- **views.py**: Handles the logic for rendering templates, processing form submissions, and managing user interactions.

### Templates
- **layout.html**: The base template that includes the common structure for all pages.
- **index.html**: The homepage template.
- **login.html**: The login page template.
- **register.html**: The registration page template.
- **profile.html**: The user profile page template.
- **nutrition.html**: The nutrition tracking page template.
- **gym_fitness.html**: The gym and fitness page template.
- **workout_abs.html**: The abs workout page template.
- **workout_arms.html**: The arms workout page template.
- **workout_back.html**: The back workout page template.
- **workout_chest.html**: The chest workout page template.
- **workout_legs.html**: The legs workout page template.
- **workout_shoulders.html**: The shoulders workout page template.
- **resources.html**: The resources page template.
- **about.html**: The about page template.

### Static Files
- **styles.css**: Contains the custom CSS styles for the application.
- **gym.js**: Contains the custom JavaScript for handling form submissions and dynamic updates.
- **images files**: Contains all the images that were used in this web application. This includes the background image on the index page, 2 menu icons, and 6 body part images in gym_fitness.html.
- **web_icon file**: Contain the web icon for the application, which was generated by favicon. 

### URLs
- **urls.py**: Defines the URL patterns for routing requests to the appropriate views.

## How to Run the Application

1. **Clone the Repository**: 

   git clone https://github.com/thaimtl/eat-to-fit.git
   
   cd eat-to-fit
3. **Install Dependencies**:
 
    pip install -r requirements.txt
4. **Apply Migrations**: 
  
    python manage.py makemigrations
   
    python manage.py migrate
6. **Run the Server**:
   
    python manage.py runserver
7. **FOR ADMINISTRATION**:
 
    python manage.py createsuperuser

### Additional Information
-The nice images of 2D body parts that you see on the Gym & Fitness page were actually generated by DALL-E 3! 

-When the user clicks on feedback, they are directed to an email box where they can email directly straight to me. 

-This is actually my capstone project for CS50 Web Development by HavardX. 

### Features to be added/improved
-For the box "description" in the adding exercise form, I will implement a custom template filters so that if the user enters a link, the hyperlink shall appear. Otherwise, it would just be plain text of blue color. I did not have the resource to do this and as you can see, each of the exercise description in the current version actually has a hyperlink no matter what was the input. If we click on this hyperlink, it would lead us to nowhere.

-The UX/UI can certainly be improved. I also think about turning the list of workout exercises into a table.

-A daily workout journal for the user to keep track of their progress can certainly be added to each of the workout template. 
