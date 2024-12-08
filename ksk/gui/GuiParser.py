from gui.Gui import GUI

class GuiParser:
    """
    Töötleb GUI tekstikastide andmetega
    """

    @staticmethod
    def värv(sisend):
        """
        Jälgib, et värv on korralikult sisestatud ja tagasab selle väärtuse korralikus vormis, kui on.
        """
        try:
            rgb = tuple([int(x) for x in sisend.strip().split(',')])
        except:
            return None
        if len(rgb) == 3:
            r, g, b = rgb
            try:
                r, g, b = int(r), int(g), int(b)
            except:
                return None
            if r < 256 and g < 256 and b < 256 and r >= 0 and g >= 0 and b >= 0:
                return (r,g,b)
        return None
    
    @staticmethod
    def nurk(sisend):
        """
        Jälgib, et nurk on korralikult sisestatud ja tagasab selle väärtuse korralikus vormis, kui on.
        """
        try:
            nurk = float(sisend)
        except:
            return None
        
        if nurk >= 0 and nurk <= 90:
            return nurk
        return None 
    
    @staticmethod
    def positiivne_number(sisend):
        """
        Jälgib, et posatiivne arv on korralikult sisestatud ja tagasab selle väärtuse korralikus vormis, kui on.
        """
        try:
            arv = float(sisend)
        except:
            return None
        if arv >= 0:
            return arv
        return None
    
    @staticmethod
    def number(sisend):
        """
        Jälgib, et arv on korralikult sisestatud ja tagasab selle väärtuse korralikus vormis, kui on.
        """
        try:
            arv = float(sisend)
        except:
            return None
        return arv