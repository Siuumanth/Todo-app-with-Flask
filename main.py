from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# only if this file runs, then only the server will run , not any other main file, so we type ==__main__