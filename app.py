from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/reverse-words", methods=["GET", "POST"])
def reverse_words():
    output = ""  # Define output variable here
    if request.method == "POST":
        input_string = request.form.get('input_data')
        if input_string:  # Check if input_string is not None or empty
            words = input_string.split()
            reverse_string = ' '.join(words[::-1])  # Join the reversed list into a string
            output = reverse_string
    
    return render_template("reverse_word.html", data=output)



@app.route("/text-replacement", methods=["GET", "POST"])
def text_replacement():
    output = ""  # Define output variable here
    if request.method == "POST":
        input_string = request.form.get('input_data')
        find = request.form.get("find")
        replace = request.form.get("replace")
        if input_string and find and replace:  # Check if input_string is not None or empty
            output = input_string.replace(find,replace)
        else:
            pass
    return render_template("replacement.html", data=output)


@app.route("/word-counter", methods=["GET", "POST"])
def word_counter():
    output = ""  # Define output variable here
    if request.method == "POST":
        input_string = request.form.get('input_data')
        if input_string:  # Check if input_string is not None or empty
            output = len(input_string.split())
        else:
            pass
    return render_template("word_counter.html", data=output)

#---shuffle function---------------#
def shuffle_word(word):

    """Shuffle the characters of a word."""
    if len(word) <= 1:
        return word  # Return the word as is if it's a single character or empty
    
    word_list = list(word)  # Convert the word to a list of characters
    random.shuffle(word_list)  # Shuffle the list in place

    return ''.join(word_list)

@app.route("/random-word", methods=["GET", "POST"])
def randoom_word():
    output = ""  # Define output variable here
    if request.method == "POST":
        input_string = request.form.get('input_data')
        option = request.form.get('exampleRadios')
        
        if input_string and option == "option1" :  # Check if input_string is not None or empty
           words = input_string.split()
           random.shuffle(words)
           randomized_text = ' '.join(words)
           output = randomized_text
        elif input_string and option == "option2":
            words = input_string.split()  # Split the paragraph into words
            shuffled_words = [shuffle_word(word) for word in words]  # Shuffle each word
            output =  ' '.join(shuffled_words) 
            
    return render_template("random_word.html", data=output)



   





if __name__ == "__main__":
    app.run(debug=True)