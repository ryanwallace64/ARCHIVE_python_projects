import turtle
import pandas
from label import Label


screen = turtle.Screen()
screen.setup(height=550, width=800)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
correct_states = 0
correct_guesses = []
label = Label()

screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
states_dict = states_data.to_dict()
missing_states = states_data.state.to_list()
x_coord_list = states_data.x.to_list()
y_coord_list = states_data.y.to_list()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?")\
        .title()
    for state in range(len(states_dict["state"])):
        if states_dict["state"][state] == answer_state:
            x = states_dict["x"][state]
            y = states_dict["y"][state]
            label.label_state(answer_state, x, y)
            correct_states += 1
            correct_guesses.append(answer_state)
            missing_states.remove(answer_state)
        if answer_state == "Exit" or correct_guesses == 50:
            game_is_on = False

print("Thank you for playing! States you still need to learn are as follows:")
print(missing_states)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()
