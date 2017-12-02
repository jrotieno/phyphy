from phyphy import *
# import ete3
# 
# 
# from ete3 import Nexml
# 
# nexml_prj = Nexml()
# nexml_prj.build_from_file("examples/data/lysin.nex")
# # 
# ext = Extractor("tests/test_data/aa.fna.LEISR.json")
# print ext.reveal_fitted_models()
# 
# print ext.reveal_branch_attributes()


# def map_branch_attribute(self, attribute_name, original_names = False, partition = None):
# def extract_model_tree(self, model, partition = None, original_names = False):
# def extract_absrel_tree(self, original_names = False, update_branch_lengths = None, p = 0.05, labels = None, ggtree = False):
# def extract_feature_tree(self, feature, original_names = False, update_branch_lengths = None, partition = None, ggtree = False):


e = Extractor("tests/test_data/BUSTED.json")
print e.extract_evidence_ratios()
# print e.extract_branch_attribute("Rate classes")
# 
# #ext = Extractor("tests/test_data/FEL_multipartitions.json")
# ext = Extractor("tests/test_data/FEL.json")
#print  ext.extract_branch_attribute("Nucleotide GTR")
# print  ext.extract_model_frequencies("Nucleotide GTR", as_dict=True)

# ext = Extractor("tests/test_data/BUSTED.json")
# print ext.extract_input_tree()
# 
# #print ext.extract_absrel_tree(update_branch_lengths="Baseline MG94xREV", ggtree=True, original_names=True, p=0.25)
# # (0564_7:0.0070474[&&NHX:Selected=1],(((((0564_11:0.00429244[&&NHX:Selected=0],0564_4:0.00627501[&&NHX:Selected=0])Node20:0.00258937[&&NHX:Selected=0],(0564_1:0.00582159[&&NHX:Selected=0],(0564_21:0.00122095[&&NHX:Selected=0],0564_5:0.00266218[&&NHX:Selected=0])Node25:0.000796464[&&NHX:Selected=0])Node23:0.00132379[&&NHX:Selected=0])Node19:0.00232443[&&NHX:Selected=0],0564_17:0.00565817[&&NHX:Selected=0])Node18:0.0010474[&&NHX:Selected=0],((0564_13:0.00540489[&&NHX:Selected=0],(0564_15:0.00260593[&&NHX:Selected=0])Node32:0.00084841[&&NHX:Selected=0])Node30:0.00152667[&&NHX:Selected=0],((0564_22:0.0070764[&&NHX:Selected=0],0564_6:0.00560434[&&NHX:Selected=0])Node36:0.00125333[&&NHX:Selected=0],0564_3:0.00623541[&&NHX:Selected=1])Node35:0.00217128[&&NHX:Selected=1])Node29:0.00111393[&&NHX:Selected=0])Node17:0.00157797[&&NHX:Selected=0],0564_9:0.00590649[&&NHX:Selected=0])Node16:0.000419203[&&NHX:Selected=0],(((0557_24:0.000787101[&&NHX:Selected=0],0557_4:0.000787068[&&NHX:Selected=0],0557_2:0.000398773[&&NHX:Selected=0])Node9:0.00204551[&&NHX:Selected=0],0557_12:0.00269259[&&NHX:Selected=0])Node8:0.00121251[&&NHX:Selected=0],((0557_21:0[&&NHX:Selected=0],0557_6:0.000391879[&&NHX:Selected=0],0557_9:0.000401729[&&NHX:Selected=0],0557_11:0.00156901[&&NHX:Selected=0],0557_13:0.000401441[&&NHX:Selected=0],0557_26:0.000793599[&&NHX:Selected=0],(0557_5:0.00117618[&&NHX:Selected=0],0557_7:0[&&NHX:Selected=0])Node53:0.000391894[&&NHX:Selected=0])Node6:0.00120876[&&NHX:Selected=0],0557_25:0.00217527[&&NHX:Selected=0])Node7:0.00101355[&&NHX:Selected=0])Separator:0.00668464[&&NHX:Selected=1])[&&NHX:Selected=0];
# 
# 
# #print ext.extract_absrel_tree()
# #(0564_7:1[&&NHX:Selected=0],(((((0564_11:1[&&NHX:Selected=0],0564_4:1[&&NHX:Selected=0])Node20:1[&&NHX:Selected=0],(0564_1:1[&&NHX:Selected=0],(0564_21:1[&&NHX:Selected=0],0564_5:1[&&NHX:Selected=0])Node25:1[&&NHX:Selected=0])Node23:1[&&NHX:Selected=0])Node19:1[&&NHX:Selected=0],0564_17:1[&&NHX:Selected=0])Node18:1[&&NHX:Selected=0],((0564_13:1[&&NHX:Selected=0],(0564_15:1[&&NHX:Selected=0])Node32:1[&&NHX:Selected=0])Node30:1[&&NHX:Selected=0],((0564_22:1[&&NHX:Selected=0],0564_6:1[&&NHX:Selected=0])Node36:1[&&NHX:Selected=0],0564_3:1[&&NHX:Selected=1])Node35:1[&&NHX:Selected=1])Node29:1[&&NHX:Selected=0])Node17:1[&&NHX:Selected=0],0564_9:1[&&NHX:Selected=0])Node16:1[&&NHX:Selected=0],(((0557_24:1[&&NHX:Selected=0],0557_4:1[&&NHX:Selected=0],0557_2:1[&&NHX:Selected=0])Node9:1[&&NHX:Selected=0],0557_12:1[&&NHX:Selected=0])Node8:1[&&NHX:Selected=0],((0557_21:1[&&NHX:Selected=0],0557_6:1[&&NHX:Selected=0],0557_9:1[&&NHX:Selected=0],0557_11:1[&&NHX:Selected=0],0557_13:1[&&NHX:Selected=0],0557_26:1[&&NHX:Selected=0],(0557_5:1[&&NHX:Selected=0],0557_7:1[&&NHX:Selected=0])Node53:1[&&NHX:Selected=0])Node6:1[&&NHX:Selected=0],0557_25:1[&&NHX:Selected=0])Node7:1[&&NHX:Selected=0])Separator:1[&&NHX:Selected=1]);
# 
# 
# #print ext.extract_absrel_tree(labels=["hello", "goodbye"])
# #(0564_7:1[&&NHX:Selected=goodbye],(((((0564_11:1[&&NHX:Selected=goodbye],0564_4:1[&&NHX:Selected=goodbye])Node20:1[&&NHX:Selected=goodbye],(0564_1:1[&&NHX:Selected=goodbye],(0564_21:1[&&NHX:Selected=goodbye],0564_5:1[&&NHX:Selected=goodbye])Node25:1[&&NHX:Selected=goodbye])Node23:1[&&NHX:Selected=goodbye])Node19:1[&&NHX:Selected=goodbye],0564_17:1[&&NHX:Selected=goodbye])Node18:1[&&NHX:Selected=goodbye],((0564_13:1[&&NHX:Selected=goodbye],(0564_15:1[&&NHX:Selected=goodbye])Node32:1[&&NHX:Selected=goodbye])Node30:1[&&NHX:Selected=goodbye],((0564_22:1[&&NHX:Selected=goodbye],0564_6:1[&&NHX:Selected=goodbye])Node36:1[&&NHX:Selected=goodbye],0564_3:1[&&NHX:Selected=hello])Node35:1[&&NHX:Selected=hello])Node29:1[&&NHX:Selected=goodbye])Node17:1[&&NHX:Selected=goodbye],0564_9:1[&&NHX:Selected=goodbye])Node16:1[&&NHX:Selected=goodbye],(((0557_24:1[&&NHX:Selected=goodbye],0557_4:1[&&NHX:Selected=goodbye],0557_2:1[&&NHX:Selected=goodbye])Node9:1[&&NHX:Selected=goodbye],0557_12:1[&&NHX:Selected=goodbye])Node8:1[&&NHX:Selected=goodbye],((0557_21:1[&&NHX:Selected=goodbye],0557_6:1[&&NHX:Selected=goodbye],0557_9:1[&&NHX:Selected=goodbye],0557_11:1[&&NHX:Selected=goodbye],0557_13:1[&&NHX:Selected=goodbye],0557_26:1[&&NHX:Selected=goodbye],(0557_5:1[&&NHX:Selected=goodbye],0557_7:1[&&NHX:Selected=goodbye])Node53:1[&&NHX:Selected=goodbye])Node6:1[&&NHX:Selected=goodbye],0557_25:1[&&NHX:Selected=goodbye])Node7:1[&&NHX:Selected=goodbye])Separator:1[&&NHX:Selected=hello]);
# 
# #print ext.extract_feature_tree("Rate classes")
# #(0564_7:1[&&NHX:Rateclasses=1],(((((0564_11:1[&&NHX:Rateclasses=2],0564_4:1[&&NHX:Rateclasses=2])Node20:1[&&NHX:Rateclasses=1],(0564_1:1[&&NHX:Rateclasses=1],(0564_21:1[&&NHX:Rateclasses=1],0564_5:1[&&NHX:Rateclasses=1])Node25:1[&&NHX:Rateclasses=1])Node23:1[&&NHX:Rateclasses=1])Node19:1[&&NHX:Rateclasses=1],0564_17:1[&&NHX:Rateclasses=1])Node18:1[&&NHX:Rateclasses=1],((0564_13:1[&&NHX:Rateclasses=1],(0564_15:1[&&NHX:Rateclasses=2])Node32:1[&&NHX:Rateclasses=1])Node30:1[&&NHX:Rateclasses=1],((0564_22:1[&&NHX:Rateclasses=1],0564_6:1[&&NHX:Rateclasses=1])Node36:1[&&NHX:Rateclasses=1],0564_3:1[&&NHX:Rateclasses=2])Node35:1[&&NHX:Rateclasses=2])Node29:1[&&NHX:Rateclasses=1])Node17:1[&&NHX:Rateclasses=1],0564_9:1[&&NHX:Rateclasses=1])Node16:1[&&NHX:Rateclasses=1],(((0557_24:1[&&NHX:Rateclasses=1],0557_4:1[&&NHX:Rateclasses=1],0557_2:1[&&NHX:Rateclasses=1])Node9:1[&&NHX:Rateclasses=1],0557_12:1[&&NHX:Rateclasses=1])Node8:1[&&NHX:Rateclasses=1],((0557_21:1[&&NHX:Rateclasses=1],0557_6:1[&&NHX:Rateclasses=1],0557_9:1[&&NHX:Rateclasses=1],0557_11:1[&&NHX:Rateclasses=1],0557_13:1[&&NHX:Rateclasses=1],0557_26:1[&&NHX:Rateclasses=1],(0557_5:1[&&NHX:Rateclasses=1],0557_7:1[&&NHX:Rateclasses=1])Node53:1[&&NHX:Rateclasses=1])Node6:1[&&NHX:Rateclasses=1],0557_25:1[&&NHX:Rateclasses=1])Node7:1[&&NHX:Rateclasses=1])Separator:1[&&NHX:Rateclasses=2]);
# 
# #print ext.extract_feature_tree("Rate classes", update_branch_lengths = "Nucleotide GTR")
# #(0564_7:0.00664844[&&NHX:Rateclasses=1],(((((0564_11:0.00434881[&&NHX:Rateclasses=2],0564_4:0.00593219[&&NHX:Rateclasses=2])Node20:0.0026739[&&NHX:Rateclasses=1],(0564_1:0.00559179[&&NHX:Rateclasses=1],(0564_21:0.00124334[&&NHX:Rateclasses=1],0564_5:0.00259957[&&NHX:Rateclasses=1])Node25:0.000863062[&&NHX:Rateclasses=1])Node23:0.00149918[&&NHX:Rateclasses=1])Node19:0.00164262[&&NHX:Rateclasses=1],0564_17:0.00600417[&&NHX:Rateclasses=1])Node18:0.00100639[&&NHX:Rateclasses=1],((0564_13:0.00534732[&&NHX:Rateclasses=1],(0564_15:0.00278489[&&NHX:Rateclasses=2])Node32:0.000565591[&&NHX:Rateclasses=1])Node30:0.00196314[&&NHX:Rateclasses=1],((0564_22:0.00686685[&&NHX:Rateclasses=1],0564_6:0.00554135[&&NHX:Rateclasses=1])Node36:0.000954793[&&NHX:Rateclasses=1],0564_3:0.00652918[&&NHX:Rateclasses=2])Node35:0.00195507[&&NHX:Rateclasses=2])Node29:0.001029[&&NHX:Rateclasses=1])Node17:0.00155756[&&NHX:Rateclasses=1],0564_9:0.00533212[&&NHX:Rateclasses=1])Node16:0.000567283[&&NHX:Rateclasses=1],(((0557_24:0.000770978[&&NHX:Rateclasses=1],0557_4:0.000770929[&&NHX:Rateclasses=1],0557_2:0.000385454[&&NHX:Rateclasses=1])Node9:0.00199212[&&NHX:Rateclasses=1],0557_12:0.00265769[&&NHX:Rateclasses=1])Node8:0.00119139[&&NHX:Rateclasses=1],((0557_21:0[&&NHX:Rateclasses=1],0557_6:0.000388349[&&NHX:Rateclasses=1],0557_9:0.000388411[&&NHX:Rateclasses=1],0557_11:0.00155424[&&NHX:Rateclasses=1],0557_13:0.000388353[&&NHX:Rateclasses=1],0557_26:0.000776809[&&NHX:Rateclasses=1],(0557_5:0.00116512[&&NHX:Rateclasses=1],0557_7:0[&&NHX:Rateclasses=1])Node53:0.000388349[&&NHX:Rateclasses=1])Node6:0.00118273[&&NHX:Rateclasses=1],0557_25:0.00219124[&&NHX:Rateclasses=1])Node7:0.000940406[&&NHX:Rateclasses=1])Separator:0.00689203[&&NHX:Rateclasses=2]);
# 
# print ext.extract_feature_tree("Rate classes", update_branch_lengths = "Nucleotide GTR", ggtree = True)
# #(0564_7:0.00664844[&&NHX:Rateclasses=1],(((((0564_11:0.00434881[&&NHX:Rateclasses=2],0564_4:0.00593219[&&NHX:Rateclasses=2])Node20:0.0026739[&&NHX:Rateclasses=1],(0564_1:0.00559179[&&NHX:Rateclasses=1],(0564_21:0.00124334[&&NHX:Rateclasses=1],0564_5:0.00259957[&&NHX:Rateclasses=1])Node25:0.000863062[&&NHX:Rateclasses=1])Node23:0.00149918[&&NHX:Rateclasses=1])Node19:0.00164262[&&NHX:Rateclasses=1],0564_17:0.00600417[&&NHX:Rateclasses=1])Node18:0.00100639[&&NHX:Rateclasses=1],((0564_13:0.00534732[&&NHX:Rateclasses=1],(0564_15:0.00278489[&&NHX:Rateclasses=2])Node32:0.000565591[&&NHX:Rateclasses=1])Node30:0.00196314[&&NHX:Rateclasses=1],((0564_22:0.00686685[&&NHX:Rateclasses=1],0564_6:0.00554135[&&NHX:Rateclasses=1])Node36:0.000954793[&&NHX:Rateclasses=1],0564_3:0.00652918[&&NHX:Rateclasses=2])Node35:0.00195507[&&NHX:Rateclasses=2])Node29:0.001029[&&NHX:Rateclasses=1])Node17:0.00155756[&&NHX:Rateclasses=1],0564_9:0.00533212[&&NHX:Rateclasses=1])Node16:0.000567283[&&NHX:Rateclasses=1],(((0557_24:0.000770978[&&NHX:Rateclasses=1],0557_4:0.000770929[&&NHX:Rateclasses=1],0557_2:0.000385454[&&NHX:Rateclasses=1])Node9:0.00199212[&&NHX:Rateclasses=1],0557_12:0.00265769[&&NHX:Rateclasses=1])Node8:0.00119139[&&NHX:Rateclasses=1],((0557_21:0[&&NHX:Rateclasses=1],0557_6:0.000388349[&&NHX:Rateclasses=1],0557_9:0.000388411[&&NHX:Rateclasses=1],0557_11:0.00155424[&&NHX:Rateclasses=1],0557_13:0.000388353[&&NHX:Rateclasses=1],0557_26:0.000776809[&&NHX:Rateclasses=1],(0557_5:0.00116512[&&NHX:Rateclasses=1],0557_7:0[&&NHX:Rateclasses=1])Node53:0.000388349[&&NHX:Rateclasses=1])Node6:0.00118273[&&NHX:Rateclasses=1],0557_25:0.00219124[&&NHX:Rateclasses=1])Node7:0.000940406[&&NHX:Rateclasses=1])Separator:0.00689203[&&NHX:Rateclasses=2])[&&NHX:Rateclasses=0];
# 
# assert 4==6
# #print ext.extract_feature_tree(["Rate classes", "LRT"], update_branch_lengths = "Nucleotide GTR")
# #(0564_7:0.00664844[&&NHX:Rateclasses=1:LRT=0],(((((0564_11:0.00434881[&&NHX:Rateclasses=2:LRT=3.96048976951],0564_4:0.00593219[&&NHX:Rateclasses=2:LRT=4.80587881259])Node20:0.0026739[&&NHX:Rateclasses=1:LRT=3.30060030447],(0564_1:0.00559179[&&NHX:Rateclasses=1:LRT=0.0105269546166],(0564_21:0.00124334[&&NHX:Rateclasses=1:LRT=0],0564_5:0.00259957[&&NHX:Rateclasses=1:LRT=4.51927751707])Node25:0.000863062[&&NHX:Rateclasses=1:LRT=0])Node23:0.00149918[&&NHX:Rateclasses=1:LRT=0])Node19:0.00164262[&&NHX:Rateclasses=1:LRT=0.153859379099],0564_17:0.00600417[&&NHX:Rateclasses=1:LRT=0])Node18:0.00100639[&&NHX:Rateclasses=1:LRT=1.64667962972],((0564_13:0.00534732[&&NHX:Rateclasses=1:LRT=0],(0564_15:0.00278489[&&NHX:Rateclasses=2:LRT=4.97443221859])Node32:0.000565591[&&NHX:Rateclasses=1:LRT=0])Node30:0.00196314[&&NHX:Rateclasses=1:LRT=2.86518293899],((0564_22:0.00686685[&&NHX:Rateclasses=1:LRT=0.114986865638],0564_6:0.00554135[&&NHX:Rateclasses=1:LRT=0])Node36:0.000954793[&&NHX:Rateclasses=1:LRT=0],0564_3:0.00652918[&&NHX:Rateclasses=2:LRT=14.0568340492])Node35:0.00195507[&&NHX:Rateclasses=2:LRT=22.65142315])Node29:0.001029[&&NHX:Rateclasses=1:LRT=1.50723222708])Node17:0.00155756[&&NHX:Rateclasses=1:LRT=2.63431127725],0564_9:0.00533212[&&NHX:Rateclasses=1:LRT=0])Node16:0.000567283[&&NHX:Rateclasses=1:LRT=0],(((0557_24:0.000770978[&&NHX:Rateclasses=1:LRT=0],0557_4:0.000770929[&&NHX:Rateclasses=1:LRT=0],0557_2:0.000385454[&&NHX:Rateclasses=1:LRT=0])Node9:0.00199212[&&NHX:Rateclasses=1:LRT=0],0557_12:0.00265769[&&NHX:Rateclasses=1:LRT=0])Node8:0.00119139[&&NHX:Rateclasses=1:LRT=1.99177154715],((0557_21:0[&&NHX:Rateclasses=1:LRT=0],0557_6:0.000388349[&&NHX:Rateclasses=1:LRT=0.662153642024],0557_9:0.000388411[&&NHX:Rateclasses=1:LRT=0],0557_11:0.00155424[&&NHX:Rateclasses=1:LRT=2.65063418443],0557_13:0.000388353[&&NHX:Rateclasses=1:LRT=0],0557_26:0.000776809[&&NHX:Rateclasses=1:LRT=0],(0557_5:0.00116512[&&NHX:Rateclasses=1:LRT=1.98893541781],0557_7:0[&&NHX:Rateclasses=1:LRT=0])Node53:0.000388349[&&NHX:Rateclasses=1:LRT=0.660753167251])Node6:0.00118273[&&NHX:Rateclasses=1:LRT=0],0557_25:0.00219124[&&NHX:Rateclasses=1:LRT=0])Node7:0.000940406[&&NHX:Rateclasses=1:LRT=1.69045394756])Separator:0.00689203[&&NHX:Rateclasses=2:LRT=14.127483568]);
# 
# 
# 
# ext = Extractor("tests/test_data/FEL.json")
# 
# print ext.extract_model_tree("Global MG94xREV")
# #((((Pig:0.192555,Cow:0.247997)Node3:0.101719,Horse:0.211311,Cat:0.273732)Node2:0.064425,((RhMonkey:0.00372054,Baboon:0.00177017)Node9:0.0259206,(Human:0,Chimp:0.00182837)Node12:0.0178636)Node8:0.109432)Node1:0.284434,Rat:0.0670088,Mouse:0.120167);
# 
# 
# ext = Extractor("tests/test_data/FEL_multipartitions.json")
# print ext.extract_model_tree("Global MG94xREV")
# #{0: '((((AF231119:0.00531869,AF231117:0.00525334)Node3:0.00173066,(AF186242:0.0017466,AF186243:0.00528072)Node6:0)Node2:0.0035056,(AF186241:0.0035303,(AF231116:0,AF187824:0.00351481)Node11:0.00350056)Node9:0.00180148)Node1:0.00352827,AF082576:0.00175291,(((AF231118:0.043318,AF234767:0.0935491)Node17:0.00780239,(AF231115:0.00178237,AF231114:0.00525221)Node20:0.00528242)Node16:0,AF231113:0.00351077)Node15:0);', 1: '(((((AF231119:0.00272572,AF231115:0)Node4:0,((AF082576:0.00274243,AF231113:0)Node8:0.00271397,AF231114:0.0110781)Node7:0.00276605)Node3:0.00271644,(AF231117:0.00298921,AF231118:0.0505183)Node12:0.00258521)Node2:0.00550172,(AF186242:0,(AF186243:0,AF234767:0.022406)Node17:0.00273366)Node15:0.00270942)Node1:0,(AF186241:0.00270936,AF231116:0)Node20:0,AF187824:0.00546772);', 2: '(AF231119:0.00194097,AF231117:0,((AF082576:0.00194116,AF231113:0.00390556)Node4:0,((((AF186242:0.00193944,AF186243:0.00393616)Node10:0.00197805,((AF186241:0,AF187824:0.00196697)Node14:0.00196212,AF231116:0)Node13:0)Node9:0.00900249,(AF231118:0.0201226,AF234767:0.061864)Node18:0.0210552)Node8:0.00286195,(AF231115:0,AF231114:0.007833)Node21:0.00583568)Node7:0)Node3:0);', 3: '((AF231119:0.000825758,AF082576:0.00164923)Node1:0,(((AF231117:0.00496535,(AF231116:0,(AF187824:0.00403545,AF231113:0.0155674)Node10:0.00850461)Node8:0.00500232)Node6:0.00334884,(AF231115:0,AF231114:0.00921003)Node13:0.00332228)Node5:0.000834802,((AF186242:0.00167319,AF186243:0.00418691)Node17:0.00165089,AF186241:0.00416815)Node16:0.00334134)Node4:0.000813033,(AF231118:0.0243313,AF234767:0.0313118)Node21:0.0190786);'}
# 
# print ext.extract_model_tree("Global MG94xREV", partition=1)
# #(((((AF231119:0.00272572,AF231115:0)Node4:0,((AF082576:0.00274243,AF231113:0)Node8:0.00271397,AF231114:0.0110781)Node7:0.00276605)Node3:0.00271644,(AF231117:0.00298921,AF231118:0.0505183)Node12:0.00258521)Node2:0.00550172,(AF186242:0,(AF186243:0,AF234767:0.022406)Node17:0.00273366)Node15:0.00270942)Node1:0,(AF186241:0.00270936,AF231116:0)Node20:0,AF187824:0.00546772);
# 
# print ext.extract_model_tree("Global MG94xREV", partition=1, original_names=True)
# #(((((AF231119~~2:0.00272572,AF231115:0)Node4:0,((AF082576:0.00274243,AF231113:0)Node8:0.00271397,AF231114:0.0110781)Node7:0.00276605)Node3:0.00271644,(AF231117:0.00298921,AF231118:0.0505183)Node12:0.00258521)Node2:0.00550172,(AF186242:0,(AF186243:0,AF234767:0.022406)Node17:0.00273366)Node15:0.00270942)Node1:0,(AF186241:0.00270936,AF231116:0)Node20:0,AF187824:0.00546772);
# 
# 