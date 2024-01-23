from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Programma Treeview - Treebase")
root.iconbitmap('good.ico')
root.geometry("1000x500")

# add some style
style = ttk.Style()

# pick a theme
style.theme_use('default')

# configure the treeview colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
# create the treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# define our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

# format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=140)
my_tree.column("Address", anchor=W, width=140)
my_tree.column("City", anchor=W, width=140)
my_tree.column("State", anchor=W, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

# add fake data
data = [
    
['Ashley', 'Ramos', 4408, '043 Laurie Club', 'Hernandezfort', 'Indiana', '32641'],
['Kimberly', 'Baker', 5279, '849 Santiago Mountain', 'Floresberg', 'Tennessee', '66406'],
['Tammie', 'Thomas', 4402, '3943 Christian Spurs', 'Bauerport', 'Alabama', '93121'],
['Latoya', 'Martinez', 3644, '6862 Lee Brook Suite 909', 'Alishire', 'Oklahoma', '89350'],
['Angela', 'Ward', 6724, '3307 Victor Spur', 'East Jamesborough', 'Rhode Island', '43102'],
['Jake', 'Martinez', 6757, '05862 Zachary Mills Apt. 679', 'Boyerport', 'Maryland', '70494'],
['Christopher', 'Palmer', 5650, '381 Wendy Estates Suite 025', 'North Matthewmouth', 'Massachusetts', '66601'],
['Amanda', 'Barr', 5603, '204 Kristen Trace', 'Brownmouth', 'Missouri', '68504'],
['Brooke', 'Lucas', 6102, '094 Joshua Mission', 'South Patricia', 'California', '60622'],
['Brenda', 'Hicks', 1429, '7553 Stephanie Glen', 'Lake Jerryburgh', 'New Mexico', '27318'],
['Kimberly', 'Gibbs', 9512, '58802 Jesse Haven', 'South Kennethberg', 'Hawaii', '61566'],
['Patrick', 'Hill', 4349, '5510 Garcia Shore', 'Jonesborough', 'Massachusetts', '23489'],
['Samantha', 'Donaldson', 5218, '1708 Evans Knoll Apt. 347', 'Ryanborough', 'Alabama', '48621'],
['Joshua', 'Cruz', 2946, '229 Wallace Green Apt. 516', 'New Kimberly', 'Washington', '23270'],
['Mark', 'Harris', 4696, '512 Andrew Loop', 'Stephenhaven', 'Illinois', '33190'],
['Steven', 'Taylor', 6690, '4269 Daniel Turnpike', 'Aaronfurt', 'Alabama', '41252'],
['Julie', 'Stark', 2546, '37098 Erin Creek', 'New Chelseaville', 'Delaware', '86629'],
['Richard', 'Gillespie', 4108, '702 Williams Mountain', 'Velazquezfort', 'New Mexico', '93363'],
['Toni', 'Logan', 2333, '4961 Hoffman Isle Suite 340', 'New Aaronborough', 'Georgia', '34000'],
['Angela', 'Woodard', 2845, '7640 Johnson Grove Apt. 898', 'Davidport', 'Arkansas', '18135'],
['Catherine', 'Huang', 3406, '4261 Costa Knolls', 'North Michele', 'Iowa', '59539'],
['Jerry', 'Harmon', 8678, '8853 Madison Underpass Apt. 189', 'West Alyssa', 'Oklahoma', '93347'],
['Michael', 'Rodriguez', 6819, '962 Skinner Lake', 'Lake Matthew', 'Alaska', '93523'],
['Barbara', 'Gray', 9624, '5746 Bell Passage', 'New Nathanborough', 'Kansas', '78033'],
['Karen', 'Davis', 9407, '924 Zachary Club', 'Port Clintonbury', 'Illinois', '87043'],
['Kathleen', 'Moore', 1963, '071 Karen Locks', 'South Brianton', 'Hawaii', '59555'],
['Brad', 'Vasquez', 6398, '397 Stephen Highway Apt. 450', 'Hayleymouth', 'Washington', '13141'],
['Eduardo', 'Bentley', 6697, '0234 Timothy Stravenue', 'New Matthew', 'Connecticut', '86435'],
['Jessica', 'Johnson', 1537, '10073 Roberts Shores Suite 844', 'Port Kathryn', 'Maine', '52448'],
['Alexandra', 'Jones', 5292, '6343 Serrano Shoal Apt. 517', 'Karenshire', 'Washington', '23650'],
['Luke', 'Howard', 7276, '703 Lee Drive Suite 545', 'Lake Ian', 'Illinois', '53186'],
['Charles', 'Ho', 3285, '44381 Shannon Village', 'New Paul', 'South Dakota', '59257'],
['Victor', 'Knight', 6216, '4732 Reed Estate Suite 906', 'South Thomas', 'Idaho', '25736'],
['Brian', 'Gibson', 3934, '65221 Kiara Flat', 'South Linda', 'Ohio', '31198'],
['Rebecca', 'Hartman', 4833, '631 Miller Keys Apt. 230', 'Port Katherine', 'Pennsylvania', '99470'],
['Cody', 'Roberts', 7781, '59831 Joyce Club Suite 288', 'East Gregorybury', 'Mississippi', '58828'],
['Matthew', 'Small', 9810, '58134 Garcia Parkways', 'Bethanyfort', 'Wyoming', '57154'],
['Nicole', 'Martin', 6572, '485 Matthew Fall', 'East Jameshaven', 'New Jersey', '53750'],
['Rose', 'Crane', 9306, '184 King Expressway Suite 655', 'Allentown', 'Indiana', '15019'],
['Christopher', 'Villarreal', 1443, '369 Rivera Ramp Suite 639', 'South Hannah', 'Virginia', '37261'],
['Lisa', 'Hill', 7908, '038 Paul Road', 'Johnsonton', 'Washington', '07368'],
['Crystal', 'Jackson', 9676, '9445 Curtis Estates Suite 882', 'Walshville', 'Illinois', '92584'],
['Angela', 'Wilson', 4971, '344 Sanchez View', 'Hallfurt', 'Michigan', '38059'],
['Victoria', 'Jennings', 8549, '162 Cynthia Summit Apt. 445', 'Reidberg', 'North Dakota', '48701'],
['Brittany', 'Calderon', 1523, '9730 Tara Mountains Apt. 119', 'North Nicholas', 'Georgia', '32008'],
['Justin', 'Valentine', 2678, '0644 Brenda Run Apt. 021', 'New Timothy', 'Vermont', '24936'],
['Gary', 'Robles', 6550, '217 Jarvis Fort', 'Theodoremouth', 'Texas', '01925'],
['Ronald', 'Flores', 5624, '371 Jones Mission', 'Port Chelseyfort', 'South Dakota', '18361'],
['Laura', 'Brooks', 9013, '4449 Denise Locks Suite 073', 'Lake Matthewstad', 'Wyoming', '90124'],
['David', 'Hunt', 6232, '75408 Megan Neck Apt. 225', 'Port Kevin', 'Montana', '62897'],
['Leslie', 'Brown', 2591, '3366 Klein Forges Suite 992', 'Clayside', 'Delaware', '15917'],
['Jennifer', 'Burnett', 2335, '75508 Laura Curve', 'Smithmouth', 'New Hampshire', '06874'],
['Jeremy', 'Nguyen', 2929, '22587 Thomas Mountains', 'Michaelville', 'Minnesota', '39967'],
['Douglas', 'Rowland', 4853, '564 Jessica Summit Apt. 443', 'Richardfort', 'Arkansas', '12412'],
['Heather', 'Wolf', 8783, '78420 Deborah Streets', 'Lunaside', 'Idaho', '42415'],
['Ryan', 'James', 9891, '22861 Nichols Dale', 'Kimberlybury', 'Wisconsin', '48191'],
['Lynn', 'Maldonado', 4260, '0472 Richardson Center Suite 667', 'South Codybury', 'Missouri', '72223'],
['Patricia', 'Brown', 7628, '63843 Howard Burgs Suite 195', 'North Bradleyhaven', 'Indiana', '93304'],
['Sharon', 'Villegas', 8366, '023 Alexis Mountains Suite 585', 'North Brian', 'Nebraska', '47250'],
['Jared', 'Parsons', 9028, '06300 Chad Roads', 'Jamesshire', 'Illinois', '07081'],
['Pamela', 'Mcmillan', 2214, '8305 Davis Inlet Suite 198', 'Port Tiffany', 'Kansas', '36435'],
['Brandy', 'Santos', 5423, '1463 Meyer Spur Apt. 953', 'Port Karaborough', 'Nebraska', '56513'],
['Stacy', 'Ware', 2397, '931 Savannah Squares', 'East William', 'North Carolina', '55356'],
['Eric', 'Mays', 8838, '40677 Green Rest', 'West Williamstad', 'Maryland', '73153'],
['Peter', 'Blake', 2045, '66818 Duffy Forges', 'Mooreville', 'Virginia', '47108'],
['Wendy', 'Nelson', 2277, '163 Mary Loaf Suite 196', 'Port Matthewhaven', 'Virginia', '59038'],
['Chad', 'Romero', 2489, '42810 Emily Lock Apt. 412', 'South James', 'Kansas', '35904'],
['Robyn', 'Roberts', 2317, '4016 Julia Throughway Apt. 273', 'North Sarah', 'Oregon', '48454'],
['Patricia', 'Conway', 9425, '132 Ruiz Fields', 'West Gregoryview', 'South Dakota', '91500'],
['Nicole', 'Strickland', 2990, '41864 Daniel Row', 'West John', 'Idaho', '97075'],
['Tyler', 'Roberts', 5664, '3611 Smith Glens Apt. 366', 'Johnfurt', 'Pennsylvania', '90110'],
['Eric', 'Hill', 1033, '8435 Stephen Courts Apt. 210', 'Clarkton', 'Utah', '51202'],
['James', 'Pope', 9547, '7362 Juan Island', 'South Erinmouth', 'Texas', '71709'],
['Sheila', 'Blake', 4095, '35181 Williams Radial Apt. 339', 'New Kristinport', 'Texas', '99511'],
['Heather', 'Shelton', 7547, '6954 Foley Stravenue Suite 256', 'East Justin', 'Mississippi', '22520'],
['Olivia', 'Jenkins', 6777, '4223 Robles Oval Suite 264', 'Port Michaelland', 'Pennsylvania', '15336'],
['Anna', 'Gonzales', 2627, '90513 Smith Plain', 'South David', 'Missouri', '11735'],
['Tina', 'Beasley', 3463, '248 Donald Turnpike', 'Angelaland', 'Iowa', '32055'],
['Stacy', 'Welch', 8983, '7206 Tammy Ports', 'Delgadofurt', 'Maryland', '33789'],
['Becky', 'Miller', 1729, '3128 Kristin Springs', 'Bowenview', 'Missouri', '12639'],
['Amber', 'Poole', 3689, '5066 Trevino Lodge Suite 645', 'New Susan', 'Michigan', '60686'],
['Paul', 'Taylor', 1899, '6610 Morrison Points Apt. 476', 'Williamville', 'Oregon', '31752'],
['Sean', 'Lambert', 5510, '43812 Haley Way', 'Adamsbury', 'Louisiana', '38150'],
['Christina', 'Mitchell', 4806, '8232 John Squares Apt. 196', 'East Michaelmouth', 'Idaho', '42686'],
['Morgan', 'Mccullough', 6402, '250 Garrison Dam', 'Conwayberg', 'Maryland', '38784'],
['Kimberly', 'Garza', 6220, '9493 Melissa Islands', 'South Pennyberg', 'Louisiana', '08975'],
['Cheryl', 'Day', 1802, '4023 Amy Dale Apt. 037', 'Port Kristina', 'Wyoming', '04308'],
['Catherine', 'Flores', 6708, '5748 Jacob Trace Suite 165', 'Christopherborough', 'South Carolina', '69816'],
['Crystal', 'Ferguson', 3927, '7957 Matthew Flat', 'North Joshuaborough', 'Hawaii', '95369'],
['Karen', 'Cortez', 4412, '423 Buchanan Square', 'South Tammytown', 'Oregon', '06687'],
['Ann', 'Arias', 8228, '1364 Cassie Union', 'Wilsonburgh', 'Indiana', '63907'],
['Michael', 'Lawrence', 1979, '97882 Bobby Port', 'East Michaelview', 'Kansas', '26554'],
['Micheal', 'Hill', 7404, '6358 David Locks', 'New Bill', 'Washington', '97768'],
['Lucas', 'Schultz', 5460, '15890 Vanessa Corner', 'Emilyton', 'Alaska', '00714'],
['Andrew', 'Jacobs', 3786, '61035 Webster Flats Apt. 500', 'South Jonathonfurt', 'Pennsylvania', '74442'],
['James', 'Smith', 1955, '161 Ethan Mountain Suite 039', 'Wernerton', 'Vermont', '85058'],
['Lindsay', 'Allen', 2808, '64343 Barnett Union', 'Allenberg', 'New York', '50725'],
['Tamara', 'Osborne', 5145, '378 Justin Squares Apt. 264', 'Christopherberg', 'South Dakota', '29096'],
['Jill', 'Myers', 6621, '4936 Shah Spur Apt. 068', 'South Linda', 'Maryland', '45539'],
['Robin', 'Chapman', 6386, '11499 Fernandez Turnpike Suite 649', 'South Zacharyburgh', 'Oregon', '49200'],    
]






# create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add our data to the screen
count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
    count += 1

# add record entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)


ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)


id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)


city_label = Label(data_frame, text="First Name")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)


state_label = Label(data_frame, text="First Name")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="First Name")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)



# add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update")
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove")
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove one")
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove many")
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up")
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down")
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Select")
select_record_button.grid(row=0, column=7, padx=10, pady=10)



root.mainloop()
