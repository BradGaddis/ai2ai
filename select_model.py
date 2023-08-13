import os


def select_model(model_dir):
    # model_dir = "./models"

    # get a list of all folders in the models directory
    model_folders = [
        f for f in os.listdir(model_dir) if os.path.isdir(os.path.join(model_dir, f))
    ]

    # print the list of model names with their index starting at 1
    for i, model_name in enumerate(model_folders):
        print(f"{i+1}. {model_name}")

    # ask the user to select a model by number
    selected_index = int(input("Enter the number of the model to select: ")) - 1
    selected_model = model_folders[selected_index]

    # check if the selected model contains a .bin file and save the path if it does
    model_bin = None
    for file in os.listdir(os.path.join(model_dir, selected_model)):
        if file.endswith(".bin"):
            model_bin = os.path.join(model_dir, selected_model, file)
            break

    if model_bin:
        print(f"Selected model binary: {model_bin}")
    else:
        print("No .bin file found in selected model directory.")

    return model_bin
