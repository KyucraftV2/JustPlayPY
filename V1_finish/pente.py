        '''
        player1 = []#la ou se range les pentes du joueur 1 avec tous les obstacles
        player2 = []#la ou se range les pentes du joueur 2 avec tous les obstacles
        
        touché = False
        for i in range(len(Map.mapa)-2):#-2 car il y a deux joueurs 
            if (Map.mapa[i][0] - Map.mapa[self.symbole][0]) == 0 :#si le calculs de la pente est une division par 0 pour le joueur 1
                gf = round( Map.mapa[i][1] - Map.mapa[self.symbole][1])*100   
                player1.append(gf)
            else: 
                gf = round((( Map.mapa[i][1] - Map.mapa[self.symbole][1])  / (Map.mapa[i][0] - Map.mapa[self.symbole][0]))*100)#calcules la pentes du joueur 1 avec les obstacles
                player1.append(gf)
            if (Map.mapa[i][0] - Map.mapa[adv.symbole][0]) == 0 :#si le calculs de la pente est une division par 0 pour le joueur 2
                gf1 = round( Map.mapa[i][1] - Map.mapa[adv.symbole][1])*100   
                player2.append(gf1)
            else: 
                gf1 = round((( Map.mapa[i][1] - Map.mapa[adv.symbole][1])  / (Map.mapa[i][0] - Map.mapa[adv.symbole][0]))*100)#calcules la pentes du joueur 2 avec les obstacles
                player2.append(gf1)
            '''
            #Si la pente est la meme cela veut dire que le tir est en direction de la cible 
            
            '''
            if player1[i] == player2[i]:#vérifie si un obstacle se trouve sur la trajectoire

                if ((Map.mapa[i][0]>Map.mapa[self.symbole][0])and(Map.mapa[i][0]>Map.mapa[adv.symbole][0]))or ((Map.mapa[i][1]>Map.mapa[self.symbole][1])and(Map.mapa[i][1]>Map.mapa[adv.symbole][1])):
                    print('L ennemi est a découvert Chef')
                    '''

                    '''
                    les pentes sont les mm pour les deux joueurs mais l obstacles se trouvent derriere eux 
                    un obstacle se trouve derriere la cible
                    '''
                    '''
                else:
                    '''
                    '''
                    les pentes sont les mm pour les deux joueurs
                    un obstacle se trouve entre la cible et le tireur
                    '''
                    touché = True
                    print('dommage tu as touché un caillou')  
                    '''