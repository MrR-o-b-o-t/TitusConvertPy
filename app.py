# from operator import index
# from flask import Flask, render_template, request, send_file
# import pandas as pd

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('updated_index.html')


# @app.route('/convert', methods=['POST'])
# def convert():
#     file = request.files['file']
#     if not file:
#         return "No file uploaded"

#     try:
#         df = pd.read_csv(file)
#         output_file = 'output.xlsx'
#         df.to_excel(output_file, index=False)
#         return send_file(output_file, as_attachment=True)
#     except Exception as e:
#         return str(e)


# if __name__ == '__main__':
#     app.run(debug=True)

from operator import index
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('updated_index.html')


@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    if not file:
        return "No file uploaded"

    try:
        df = pd.read_csv(file)

        # df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
        df['Full Name'] = '=HYPERLINK(' '"' + df['Profile URL'] + '"' + \
            ',' + '"' + df['First Name'] + ' ' + df['Last Name'] + '"' + ')'

        df.drop(['First Name', 'Last Name', 'Headline',
                'Notes', 'Profile URL', 'Active Project'], axis=1, inplace=True)
        df.set_index('Full Name', inplace=True)
        titles = list(df.columns)
        titles[1], titles[2] = titles[2], titles[1]
        df = df[titles]
        df.dropna(axis=1, how='all', inplace=True)
        output_file = 'output.xlsx'
        df.to_excel(output_file)
        return send_file(output_file, as_attachment=True)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
