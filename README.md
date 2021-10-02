const Discord = require("discord.js")
const bot =  new Discord.Client({
    intents: [
        Discord.Intents.FLAGS.GUILDS,
        Discord.Intents.FLAGS.GUILD_MESSAGES
    ]
});
bot.on("ready", () => 
{
    console.log("bon toutou");
    console.log("vive va vie");
});
const prefix =  "$";
bot.on("messageCreate", message => {
    if(message.author.bot) return;
    if(message.content === prefix + "Miku")
    {
        message.reply("**Voix japonaise : Miku Itō, Miku Nakano est la troisième sœur aux cheveux mi-longs et au regard « sans émotion », elle porte aussi en temps normal un casque audio spécifique autour de son cou. D une personnalité calme et passive, elle a peu d amis et un intérêt pour les seigneurs de guerre d époques spécifiques de l histoire japonaise. Très mauvaise cuisinière, elle a commencé à se concentrer pour s améliorer dans ce domaine après que Fūtarō ait déclaré qu il préférait les filles sachant cuisiner.**");
    }
    else 
    {
        
    }
    if(message.content === prefix + "help")
    {
        message.reply("les commande disponible actuellement sont : Miku, Nino, Ichika, synopsis, Yotsuba, Itsuki, Fūtarō Uesugi, Raiha, bio, Saison 1, Saison2")
    }
    else
    {
       
    }
    if(message.content === prefix + "synopsis")
    {
        message.reply("```The Quintessential Quintuplets (du le titre original Go-toubun no hanayome), c'est l'histoire de la rencontre entre le discret Fûtarô et les cinq sœurs Nakano. Résumé de l'éditeur : Fûtarô, un lycéen brillant mais fauché, décroche un petit boulot de rêve : professeur particulier pour une famille fortunée.```")
    }
    else
    {

    }
    if(message.content === prefix + "Ichika")
    {
        message.reply("**Voix japonaise : Kana Hanazawa, Ichika Nakano est la sœur aînée aux cheveux courts qui ne porte pas d accessoire. Elle est le modèle de la grande sœur par excellence : une combinaison de bienveillance, de réflexion, de sagesse et de plaisanterie. Elle aime dormir et sa chambre se retrouve souvent dans un énorme désordre. Elle aspire à devenir une actrice de cinéma et y consacre la majeure partie de son temps et de ses ressources, au point de devoir quitter l école pour se concentrer sur sa carrière d actrice**")
    }
    else
    {

    }
    if(message.content === prefix + "Nino")
    {
        message.reply("**Voix japonaise : Ayana Taketatsu, Nino Nakano est la seconde sœur aux longs cheveux avec deux rubans ressemblant à des papillons sur les côtés. Elle porte des lentilles de contact depuis trois ans en raison de sa mauvaise vue. Bien qu elle soit attentionnée et enjouée avec ses sœurs, elle montre une personnalité grincheuse, parfois grossière et agressive à des personnes extérieures à leur groupe. Elle est à la mode et habile en cuisine, laissant entendre qu elle rêvait de devenir chef. L unité des sœurs lui est primordiale ; considérant Fūtarō comme un intrus, elle a pris des mesures extrêmes, parfois illégales, pour tenter de le bannir de son appartement**")
    }
    else
    {

    }
    if(message.content === prefix + "Yotsuba")
    {
        message.reply("**Voix japonaise : Ayane Sakura, est la quatrième sœur à la coupe au carré portant un ruban vert en forme d oreilles de lapin. Toujours joyeuse et amicale, elle est aussi une bonne sportive, mais sa personnalité constamment dynamique peut agacer les autres. Elle obtient souvent des 0 aux tests scolaires. Ses actions suggèrent généralement soit une absence totale de pensée, soit des plans complexes et inconscients bien au-delà de tout ce que les autres personnages peuvent imaginer. Elle est la seule à accepter immédiatement Fūtarō comme tuteur. Elle soutient et porte toujours son attention aux autres, en particulier à ses sœurs et Futaro. Elle a aussi la mauvaise habitude de faire passer les besoins des autres avant les siens.**")
    }
    else
    {

    }
    if(message.content === prefix + "Itsuki")
    {
        message.reply("**Voix japonaise : Inori Minase, est la benjamine des cinq sœurs. Elle a de longs cheveux avec un ahoge expressif et deux épingles à cheveux en forme d étoiles à côté de ses yeux. Elle a une personnalité miroir : toujours amicale avec ses connaissances et ses camarades de classe, mais la présence de Fūtarō, qui l avait frustrée et insultée lors de leur rencontre au lycée, la met immédiatement en rogne. Elle adore manger et étudie sérieusement, même si ses méthodes doivent être améliorées. Depuis qu elle était petite, elle était proche de sa mère, Rena. Après son décès, elle a décidé de faire face à sa perte en essayant de remplacer Rena en tant que figure maternelle des quintuplées, avec des résultats infructueux.**")
    }
    else
    {

    }
    if(message.content === prefix + "Fūtarō Uesugi")
    {
        message.reply("**Voix japonaise : Yoshitsugu Matsuoka1,2, Mutsumi Tamura (ja) (enfant), Un lycéen japonais à la personnalité franche qui obtient d excellentes notes mais qui n a pas d amis. Il vit dans un petit appartement avec sa famille démunie composée d un père paresseux et désordonné, généralement ignoré, et d une jeune sœur assidue, Raiha ; elle est la seule personne qui prend soin de Fūtarō et vice versa. Fūtarō est toujours sérieux et dévoué à ses efforts pour aider les sœurs Nakano à améliorer leurs résultats scolaires, mais il peut parfois se montrer prétentieux ou moqueur. Dans son carnet d élève, il garde une photo d une fille rencontrée à Kyoto alors qu il était enfant, qui a été la raison l ayant poussé à étudier ; cette fille se révélant être l une des quintuplées Nakano.**")
    }
    else
    {

    }
    if(message.content === prefix + "Raiha")
    {
        message.reply("**Voix japonaise : Natsumi Takamori (ja), est la petite sœur enjouée de Fūtarō ; étant la seule femme et la plus soucieuse de sa famille, elle est en réalité à la tête de la petite famille. Ses expressions faciales mignonnes vont souvent influencer le cœur des autres. Appréciant le dur travail que fait son frère pour sa famille, elle retarde parfois le dîner jusqu à son retour tardif à la maison pour pouvoir lui préparer son repas préféré.**")
    }
    else
    {

    }
    if(message.content === prefix + "bio")
    {
        message.reply("***Étant physiquement identiques, elles ont toutes de grands yeux bleus, des cheveux légèrement rougeâtres, un joli visage expressif et une silhouette bien proportionnée. Malgré leurs coiffures différentes, les sœurs sont très bonnes pour s'imiter mutuellement et le font souvent pour des farces ou pour des raisons pratiques. Elles sont nées le 5 mai.***")
    }
    else
    {

    }
    if(message.content === prefix + "Saison 1")
    {
        message.reply("```https://voiranime.com/anime/5-toubun-no-hanayome/5-toubun-no-hanayome-01-vostfr/```")
    }
    else
    {

    }
    if(message.content === prefix + "Saison 2")
    {
        message.reply("```https://voiranime.com/anime/5-toubun-no-hanayome-ii/5-toubun-no-hanayome-ii-01-vostfr/```")
    }
    else
    {

    }
})
bot.login('NTEyMjk0ODI4NDQ5NzI2NDky.W-xFvQ.NleR7SSwtXwna89KuzEMHmUZHEc')
