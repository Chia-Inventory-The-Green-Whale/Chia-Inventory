# add list of item and their attribute bonus here:
# item_list = [item1, item2, etc...]


Water_Chia_Slime_list = [
"Chia Slime #406",
"Chia Slime #407",
"Chia Slime #408",
"Chia Slime #409",
"Chia Slime #410",
"Chia Slime #411",
"Chia Slime #412",
"Chia Slime #413",
"Chia Slime #414",
"Chia Slime #415",
"Chia Slime #416",
"Chia Slime #417",
"Chia Slime #418",
"Chia Slime #419",
"Chia Slime #420",
"Chia Slime #421",
"Chia Slime #422",
"Chia Slime #423",
"Chia Slime #424",
"Chia Slime #425",
"Chia Slime #426",
"Chia Slime #427",
"Chia Slime #428",
"Chia Slime #429",
"Chia Slime #430",
"Chia Slime #431",
"Chia Slime #432",
"Chia Slime #433",
"Chia Slime #434",
"Chia Slime #435",
"Chia Slime #436",
"Chia Slime #437",
"Chia Slime #438",
"Chia Slime #439",
"Chia Slime #440",
"Chia Slime #441",
"Chia Slime #442",
"Chia Slime #443",
"Chia Slime #444",
"Chia Slime #445",
"Chia Slime #446",
"Chia Slime #447",
"Chia Slime #448",
"Chia Slime #449",
"Chia Slime #450",
"Chia Slime #451",
"Chia Slime #452",
"Chia Slime #453",
"Chia Slime #454",
"Chia Slime #455"]

SlipStream_Chia_Slime_list = [
"Chia Slime #410",
"Chia Slime #411",
"Chia Slime #414",
"Chia Slime #415",
"Chia Slime #416",
"Chia Slime #422",
"Chia Slime #424",
"Chia Slime #425",
"Chia Slime #426",
"Chia Slime #427",
"Chia Slime #430",
"Chia Slime #431",
"Chia Slime #432",
"Chia Slime #433",
"Chia Slime #435",
"Chia Slime #436",
"Chia Slime #437",
"Chia Slime #440",
"Chia Slime #442",
"Chia Slime #447",
"Chia Slime #450",
"Chia Slime #452",
"Chia Slime #455"]

#These (Healing/Identify/DefensiveAura) are to be ADDED to exsisting lists
Healing_Chia_Slime_list = [
"Chia Slime #407",
"Chia Slime #408",
"Chia Slime #417",
"Chia Slime #421",
"Chia Slime #439",
"Chia Slime #441",
"Chia Slime #443",
"Chia Slime #444",
"Chia Slime #445",
"Chia Slime #446",
"Chia Slime #451",
"Chia Slime #453",
"Chia Slime #454"]

Identify_Chia_Slime_list = [
"Chia Slime #406",
"Chia Slime #409",
"Chia Slime #413",
"Chia Slime #418",
"Chia Slime #428",
"Chia Slime #434",
"Chia Slime #438",
"Chia Slime #448",
"Chia Slime #449"
]

DefensiveAura_Chia_Slime_list = [
"Chia Slime #412",
"Chia Slime #419",
"Chia Slime #420",
"Chia Slime #423",
"Chia Slime #429"]


# describe the attribute here, e.g. item_list 1, feature fire, +1 str

#Water Slimes base bonus: 
 if stats.familiar in Water_Chia_Slime_list:
        stats.int = stats.int + 2
        stats.str = stats.str - 1
        stats.con = stats.con - 1
#in-line with Water Slimes magical nature they give their owners a boost to their own magical capabilities, at the sacrifice of physical attributes.

#Slip Stream Power:
if stats.familiar in SlipStream_Chia_Slime_list:
        SlipStream_castchance = random.randint(1, 20)
        if SlipStream_castchance in [17, 18, 19, 20]:
            stats.bash = stats.bash + 1
#The Water Slime shoots a burst of water, unbalancing your foe and causing them to slip and collapse.
