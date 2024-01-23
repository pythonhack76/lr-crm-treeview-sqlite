from tkinter import *
from tkinter import ttk

root = Tk() 
root.title("Programma Treeview - Treebase")
root.iconbitmap('good.ico')
root.geometry("1000x500")

#add some style
style = ttk.Style() 

#pick a theme
style.theme_use('default')

#configure the treeview colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                roeheight=25,
                fieldbackground="#D3D3D3")

#Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

#crete a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

#create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
#create the treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack() 

#configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

#define our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

#format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.colum("First Name", anchor=W, width=140)
my_tree.colum("Last Name", anchor=W, width=140)
my_tree.colum("ID", anchor=CENTER, width=140)
my_tree.colum("Address", anchor=W, width=140)
my_tree.colum("City", anchor=W, width=140)
my_tree.colum("State", anchor=W, width=140)
my_tree.colum("Last Name", anchor=W, width=140)
my_tree.colum("Zipcode", anchor=CENTER, width=140)

#create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="", anchor=W)
my_tree.heading("Last Name", text="", anchor=W)
my_tree.heading("ID", text="", anchor=CENTER)
my_tree.heading("Addrees", text="", anchor=CENTER)
my_tree.heading("City", text="", anchor=CENTER)
my_tree.heading("State", text="", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

#add fake data

data = ["Tina","Walton", 20, "654 Stree Ave.", "Chicago","Illinois",20020 ]
['Jeremy', 'Butler', 8804, '1182 Tiffany Mews Apt. 620', 'Weaverburgh', 'Colorado', '40543']
['Leslie', 'Webb', 2973, '12642 Sanchez Prairie', 'Port Scott', 'New Jersey', '06314']
['Jorge', 'Barr', 9149, '70550 Mike Streets Apt. 323', 'Port Kelly', 'Illinois', '42062']
['Brett', 'Sawyer', 1301, '213 Colleen Street Suite 898', 'Lake Robert', 'California', '75145']
['Robert', 'Wilson', 8134, '904 Vanessa Courts Apt. 843', 'New Lesliemouth', 'Virginia', '75590']
['Scott', 'Mercer', 2462, '06532 Darren Highway', 'Port Crystal', 'Louisiana', '47762']
['Nicole', 'Miller', 6018, '04490 William Manors', 'Fletcherhaven', 'Oregon', '14095']
['Austin', 'Brown', 8266, '023 Williams Burgs Apt. 936', 'Clarkfort', 'Washington', '31534']
['Richard', 'French', 5808, '868 Moran Pike Suite 182', 'Ellisland', 'West Virginia', '01525']
['Karen', 'Wood', 4372, '164 Craig Landing Apt. 214', 'East Tamara', 'Hawaii', '29775']
['Michael', 'Thomas', 6546, '3899 Hoffman Mission Apt. 575', 'Hillview', 'New Jersey', '48695']
['Yvonne', 'Schmidt', 1601, '684 Vincent Ridges', 'Port Christopher', 'West Virginia', '73517']
['James', 'Thomas', 7901, '09707 Jeffrey Extension', 'Kevinfurt', 'Virginia', '42255']
['Kevin', 'Kirby', 8743, '970 Dean Brooks', 'West Johnborough', 'Ohio', '73334']
['Sandra', 'Edwards', 2395, '7825 Nash Motorway Apt. 726', 'Mcintyremouth', 'New Hampshire', '89652']
['Jeff', 'Brooks', 6171, '31729 Ricky Way', 'West Markfort', 'Rhode Island', '18783']
['Brittany', 'Shaw', 3911, '20423 Baxter Ramp', 'West Barbara', 'Missouri', '75806']
['Ronald', 'Johnson', 6305, '6871 James Estates Suite 062', 'Bryantberg', 'Idaho', '16458']
['Jordan', 'Parker', 3371, '51380 Michael Knolls', 'Port Amychester', 'Illinois', '41739']
['John', 'Edwards', 2918, '72672 Curry Path', 'Ericaborough', 'Louisiana', '21366']
['Diane', 'Davis', 1598, '8236 Andrew Mountain Suite 002', 'Kingfurt', 'Indiana', '86279']
['Paul', 'Martinez', 9161, '304 Phillips Viaduct Apt. 614', 'Juarezstad', 'Wyoming', '34156']
['Michelle', 'Scott', 1663, '500 Jeffrey Knolls Suite 046', 'North Wanda', 'Delaware', '76322']
['Kimberly', 'Obrien', 1040, '837 Alexander Park Suite 036', 'Bishopside', 'Idaho', '89980']
['Manuel', 'Randall', 6884, '886 Ball Centers Apt. 400', 'Mariahborough', 'Kentucky', '10514']
['Aaron', 'Smith', 9967, '46732 Justin Mews', 'Olsonton', 'Michigan', '93765']
['Richard', 'Romero', 9019, '2749 Tate Loaf', 'Matthewsfort', 'Ohio', '91678']
['Valerie', 'Barnes', 8974, '989 Robert Union', 'Torresview', 'Florida', '49814']
['Robert', 'Holloway', 2549, '39861 Johnson Knolls', 'New Jose', 'New York', '17455']
['Christine', 'Smith', 4123, '507 Sandra Garden Suite 636', 'Darrellborough', 'Minnesota', '05091']
['Catherine', 'Stevens', 3432, '899 Rhonda Cape Suite 345', 'Kimville', 'Illinois', '58305']
['Karen', 'Whitaker', 4612, '750 Roberta Ranch Suite 335', 'Richardsonberg', 'Virginia', '51242']
['Lori', 'Lee', 8925, '402 Ian Isle', 'Georgemouth', 'Maryland', '59952']
['Ashley', 'Grant', 9063, '97512 Amanda Lane', 'South Matthew', 'Indiana', '41475']
['Todd', 'Horn', 8585, '30747 Daugherty Estate Suite 332', 'Rubiostad', 'South Dakota', '07799']
['Alexander', 'Howard', 8953, '88823 Thomas Locks', 'Beasleyside', 'Delaware', '39647']
['David', 'Matthews', 4672, '5521 Sanders Center', 'Ashleyhaven', 'Kentucky', '96362']
['Cassandra', 'Serrano', 8792, '34998 Hunt Camp Suite 327', 'Sanchezville', 'Illinois', '58318']
['Nicole', 'Pham', 9416, '196 Mcdaniel Island Suite 779', 'Gonzalesborough', 'Tennessee', '68468']
['William', 'Graham', 9082, '97144 Roy Meadow', 'Port Brandon', 'Arizona', '91189']
['Megan', 'Chen', 4756, '81221 Williams Overpass Suite 644', 'Lake Robertfurt', 'Oregon', '75574']
['Tricia', 'Hall', 9847, '46186 Molina Lane', 'Stevensonhaven', 'Michigan', '74895']
['Rita', 'Gray', 8672, '675 Donald Circle Suite 661', 'Port Joannfurt', 'North Carolina', '53560']
['Linda', 'Burns', 2936, '96683 Ferguson Ramp', 'Fisherside', 'South Carolina', '62697']
['Jeffrey', 'Stevens', 8073, '28868 Hicks Fort Suite 525', 'Morrisonside', 'Rhode Island', '17246']
['Benjamin', 'Castillo', 5890, '13651 Ann Roads Suite 430', 'West Brian', 'Arkansas', '11568']
['Lisa', 'Sweeney', 8892, '9102 Hodge Lodge', 'Rebeccaside', 'Arkansas', '59299']
['Mark', 'Gutierrez', 1592, '555 Jennifer Plains Suite 369', 'New Briannabury', 'Colorado', '25526']
['Cynthia', 'Sanchez', 6669, '38224 Le Shores', 'West Jamesmouth', 'Pennsylvania', '22951']
['Ricky', 'Reyes', 4261, '0092 Marie Lakes', 'Port Andrea', 'Tennessee', '35097']
['Lauren', 'Miller', 9376, '57585 Cassandra Rapids', 'Georgebury', 'Michigan', '13976']
['Joseph', 'Mitchell', 5224, '10560 Scott Falls', 'East James', 'Oregon', '74332']
['Meghan', 'Abbott', 8030, '941 Teresa Street', 'New Richard', 'Indiana', '48702']
['Johnathan', 'Scott', 2413, '710 Krystal Locks', 'Weaverstad', 'South Carolina', '52478']
['John', 'Miller', 9874, '6193 Proctor Way Apt. 454', 'Port Tiffany', 'Florida', '98434']
['Chad', 'Lucas', 7729, '59245 Patrick Way Suite 535', 'Barrstad', 'Montana', '55209']
['Whitney', 'Alvarez', 5364, '728 Francis Flat Apt. 262', 'Traciefort', 'Nevada', '53307']
['Michael', 'Hays', 1412, '437 Diana Road', 'West Katherinechester', 'Vermont', '79432']
['Robert', 'Turner', 8867, '5932 Deborah Curve', 'Rosetown', 'South Carolina', '34281']
['Richard', 'Turner', 9116, '479 Francisco Isle', 'South Mary', 'Kentucky', '20270']
['Christopher', 'Patterson', 1760, '629 Richard Tunnel', 'Brendafurt', 'Arizona', '45343']
['Megan', 'Sanders', 8679, '560 Buck Trace Suite 699', 'West Suzannehaven', 'Utah', '11404']
['Roy', 'Gallagher', 9883, '6976 Wong Village Apt. 158', 'Johnstonshire', 'Hawaii', '21483']
['Brandon', 'Chen', 2059, '85501 Shannon Lock Apt. 371', 'Fieldsmouth', 'Georgia', '61307']
['Jay', 'Hammond', 5500, '0516 Morris Club', 'West Noahtown', 'Alabama', '82741']
['Lisa', 'Fields', 9593, '5231 Taylor Union Apt. 607', 'Port Paul', 'Tennessee', '02004']
['Maria', 'Parker', 2139, '0687 Edward Track', 'South Timothystad', 'New Hampshire', '82831']
['Donna', 'White', 8355, '1424 Stephanie Mountains Suite 719', 'East Derek', 'Wisconsin', '50219']
['Cynthia', 'Ross', 8043, '9452 Karen Knoll Apt. 783', 'Danielberg', 'Tennessee', '94070']
['Amy', 'Brock', 8549, '49127 Ross Summit', 'Lisaberg', 'Tennessee', '12275']
['Daniel', 'Thompson', 5885, '70983 Amanda Grove Suite 594', 'Lewisview', 'New Mexico', '81904']
['Mark', 'Diaz', 8968, '94307 Brooks Meadows Apt. 737', 'East Suzanne', 'Michigan', '68521']
['Daniel', 'Barron', 4082, '6287 Brown Motorway Suite 991', 'Amandastad', 'Connecticut', '31003']
['Brian', 'Hansen', 6919, '352 Ramirez Crescent', 'North Davidside', 'Michigan', '67856']
['Daniel', 'Krause', 1664, '096 Davis Creek Apt. 081', 'South Jenniferview', 'New Mexico', '85482']
['Angela', 'Carter', 7498, '51198 Wilson Forest', 'North Stacy', 'North Dakota', '74186']
['Thomas', 'Griffith', 2311, '3161 Keith Crescent', 'North Caitlynside', 'Oklahoma', '25803']
['Debra', 'Williamson', 2842, '59189 Leslie Trail', 'New Adamport', 'North Dakota', '43185']
['David', 'Sandoval', 4775, '58679 Ortega Street Apt. 372', 'Tracyton', 'Oklahoma', '42375']
['Victoria', 'Townsend', 5325, '6783 Adam Court Apt. 889', 'Parkerchester', 'Oregon', '64828']
['Katherine', 'Morris', 3380, '739 Hale Lights', 'North Erichaven', 'Indiana', '64810']
['Anne', 'Torres', 4401, '1169 Luis Place Apt. 042', 'Katherineshire', 'New York', '46213']
['Deborah', 'Parker', 3938, '9966 Hernandez Dam Apt. 438', 'East Christopherchester', 'New Mexico', '13015']
['Brenda', 'Berry', 5089, '418 Duran Ports', 'Bennettton', 'Wyoming', '92189']
['Roger', 'Frazier', 4969, '3209 Kyle Meadows', 'Deanburgh', 'Wyoming', '83162']
['Sharon', 'Garcia', 1160, '23923 Peterson Camp Suite 622', 'North Ryan', 'Tennessee', '19866']
['Latoya', 'Townsend', 7744, '22584 Ashley Expressway Suite 502', 'Campbellstad', 'Indiana', '57359']
['Adam', 'Thomas', 8322, '1498 Cunningham Summit', 'East Mary', 'Montana', '81599']
['Donna', 'Anderson', 5051, '4558 Long Vista', 'Williamville', 'Colorado', '17218']
['Carlos', 'Martinez', 6496, '463 Marc Divide Suite 744', 'Brandychester', 'Nevada', '54576']
['Christopher', 'Kim', 9079, '798 Benson Point', 'Mooreburgh', 'Georgia', '19986']
['Wanda', 'Martin', 5175, '2210 Anthony Street Suite 847', 'Nicoleview', 'Illinois', '06042']
['Rachael', 'Daniel', 1907, '2424 Brown Orchard', 'Audreychester', 'Florida', '37019']
['Daniel', 'Thomas', 6396, '100 Amy Plains Suite 823', 'East Jasmine', 'Nebraska', '60581']
['Calvin', 'Gomez', 1075, '42916 Brown Greens Apt. 182', 'Jessicaport', 'West Virginia', '29340']
['Alicia', 'Norman', 5375, '1630 Ernest Path', 'Teresaland', 'Louisiana', '70880']
['Matthew', 'Sellers', 9276, '4104 Joshua Road', 'Johnsonmouth', 'Maryland', '38562']
['Randall', 'Harris', 4441, '361 Tina Mountain', 'North Susan', 'Pennsylvania', '56457']
['John', 'Martin', 9252, '15149 Manning Fords Apt. 208', 'Port Tracyburgh', 'Oklahoma', '19253']
['Brandi', 'Simpson', 9086, '20035 Griffith Skyway Suite 614', 'New David', 'Ohio', '96976']

#create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

#Add our data to the screen
global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow',))
    else:
         my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow',))
    # 
#add record entry boxes 


#add buttons


root.mainloop() 

