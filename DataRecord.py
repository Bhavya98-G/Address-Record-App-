from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title('Update A Record')
root.geometry('400x400') 

# create a database or connect to one
conn = sqlite3.connect('addressBook.db')

# Create a cursor
c = conn.cursor()
 

#Create table
c.execute("""CREATE TABLE address(
          firstName text,
          lastName text,
          address text,
          city text,
          state text,
          zipcode integer
          )       
          """)

#Create Submit Function for Database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    c = conn.cursor()

    # Insert into Table
    c.execute("INSERT INTO address VALUES (:fName , :lName , :address ,:city ,:state ,:zipcode)",
              {
                'fName': fName.get(),
                'lName': lName.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()  
                  })

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()
     
    # Clear the text box
    fName.delete(0,END)
    lName.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create query Function
def query():
    # create a database or connect to one
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM address") 
    records = c.fetchall()
    #print(records)
    printRecords = ''

    for record in records:
        printRecords += str(record[0]) + ' ' +str(record[1])+ ' '+'\t'+ str(record[6]) + '\n'

    queryLabel = Label(root , text = printRecords)
    queryLabel.grid(row=12,column=0,columnspan=2)

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

# Create Function to delete a record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM address WHERE oid = " + deleteBox.get())

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

# Create update function to update a record
def save():
    # create a database or connect to one
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    c = conn.cursor()

    recordId = deleteBox.get()

    c.execute("""UPDATE address SET
              firstName = :first,
              lastName = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode

              WHERE oid = :oid""",
              {'first':fNameEditor.get(),
               'last': lNameEditor.get(),
               'address' : addressEditor.get(),
               'city': cityEditor.get(),
               'state': stateEditor.get(),
               'zipcode': zipcodeEditor.get(),

               'oid': recordId
              }
              
              )

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

    editor.destroy()

def update():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry('400x250')
    # create a database or connect to one
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    c = conn.cursor()

    recordId = deleteBox.get()

    # Query the database
    c.execute("SELECT * FROM address where oid = "+ recordId) 
    records = c.fetchall()

    #Create Global Variables for text box names
    global fNameEditor 
    global lNameEditor 
    global addressEditor 
    global cityEditor 
    global stateEditor 
    global zipcodeEditor 



 
    # Create Text Boxes

    fNameEditor = Entry(editor, width=30)
    fNameEditor.grid(row=0, column = 1, padx=20, pady=(10,0))

    lNameEditor = Entry(editor, width=30)
    lNameEditor.grid(row=1, column = 1, padx=20)

    addressEditor = Entry(editor, width=30)
    addressEditor.grid(row=2, column = 1, padx=20)

    cityEditor = Entry(editor, width=30)
    cityEditor.grid(row=3, column = 1, padx=20)

    stateEditor = Entry(editor, width=30)
    stateEditor.grid(row=4, column = 1, padx=20)

    zipcodeEditor = Entry(editor, width=30)
    zipcodeEditor.grid(row=5, column = 1, padx=20) 

    # Create Text Box Labels
    fNameLabelEditor = Label(editor,text='First Name')
    fNameLabelEditor.grid(row=0,column=0, pady=(10,0))

    lNameLabelEditor = Label(editor,text='Last Name')
    lNameLabelEditor.grid(row=1,column=0)

    addressLabelEditor = Label(editor,text='Address')
    addressLabelEditor.grid(row=2,column=0)

    cityLabelEditor = Label(editor,text='City')
    cityLabelEditor.grid(row=3,column=0)

    stateLabelEditor = Label(editor,text='State')
    stateLabelEditor.grid(row=4,column=0)

    zipcodeLabelEditor = Label(editor,text='Zip Code')
    zipcodeLabelEditor.grid(row=5,column=0)

    #Loop thru results
    for record in records:
        fNameEditor.insert(0,record[0])
        lNameEditor.insert(0,record[1])
        addressEditor.insert(0,record[2])
        cityEditor.insert(0,record[3])
        stateEditor.insert(0,record[4])
        zipcodeEditor.insert(0,record[5])

    #Create a Save Button
    saveBtn = Button(editor, text='Save Record', command=save)
    saveBtn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=145)




# Create Text Boxes

fName = Entry(root, width=30)
fName.grid(row=0, column = 1, padx=20, pady=(10,0))

lName = Entry(root, width=30)
lName.grid(row=1, column = 1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column = 1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column = 1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column = 1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column = 1, padx=20) 

deleteBox = Entry(root,width=30)
deleteBox.grid(row=9,column=1,pady=5)

# Create Text Box Labels
fNameLabel = Label(root,text='First Name')
fNameLabel.grid(row=0,column=0, pady=(10,0))

lNameLabel = Label(root,text='Last Name')
lNameLabel.grid(row=1,column=0)

addressLabel = Label(root,text='Address')
addressLabel.grid(row=2,column=0)

cityLabel = Label(root,text='City')
cityLabel.grid(row=3,column=0)

stateLabel = Label(root,text='State')
stateLabel.grid(row=4,column=0)

zipcodeLabel = Label(root,text='Zip Code')
zipcodeLabel.grid(row=5,column=0)

deleteBoxLabel = Label(root,text='Select ID ')
deleteBoxLabel.grid(row=9,column=0,pady=5)

# Create Submit Button
submitBtn = Button(root,text='Add record to Database',command=submit)
submitBtn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

# Create a Query Button
queryBtn = Button(root, text='Show Records', command=query)
queryBtn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a delete Button
deleteBtn = Button(root, text='Delete Record', command=delete)
deleteBtn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a Update Button
updateBtn = Button(root, text='Update Record', command=update)
updateBtn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=133)


#Commit changes
conn.commit()

#Close Connection
conn.close() 

root.mainloop()
