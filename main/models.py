from django.db import models

# Create your models here.

class usser(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    img = models.ImageField(upload_to='img/', null=True, blank=True)

    img1 = models.ImageField(upload_to='img1/', null=True, blank=True)
    img2 = models.ImageField(upload_to='img2/', null=True, blank=True)
    img3 = models.ImageField(upload_to='img3/', null=True, blank=True)
    img4 = models.ImageField(upload_to='img4/', null=True, blank=True)
    img5 = models.ImageField(upload_to='img5/', null=True, blank=True)
    img6 = models.ImageField(upload_to='img6/', null=True, blank=True)
    img7 = models.ImageField(upload_to='img7/', null=True, blank=True)
    img8 = models.ImageField(upload_to='img8/', null=True, blank=True)

    serv1 = models.ImageField(upload_to='serv1/', null=True, blank=True)
    serv2 = models.ImageField(upload_to='serv2/', null=True, blank=True)
    serv3 = models.ImageField(upload_to='serv3/', null=True, blank=True)

    up_arrow = models.ImageField(upload_to='up_arrow/', null=True, blank=True)

    team1 = models.ImageField(upload_to='team1/', null=True, blank=True)
    team2 = models.ImageField(upload_to='team2/', null=True, blank=True)
    team3 = models.ImageField(upload_to='team3/', null=True, blank=True)
    team4 = models.ImageField(upload_to='team4/', null=True, blank=True)

    testimonial1 = models.ImageField(upload_to='testimonial1/', null=True, blank=True)
    testimonial2 = models.ImageField(upload_to='testimonial2/', null=True, blank=True)
    testimonial3 = models.ImageField(upload_to='testimonial3/', null=True, blank=True)
    testimonial4 = models.ImageField(upload_to='testimonial4/', null=True, blank=True)
    testimonial5 = models.ImageField(upload_to='testimonial5/', null=True, blank=True)
    testimonial6 = models.ImageField(upload_to='testimonial6/', null=True, blank=True)

    def __str__(self):
        return self.name

class Sitetext(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)

    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)

    serv1_title = models.CharField(max_length=255, default='Off The Ground Off The Ground')
    serv1_text = models.CharField(max_length=255, default="Perfect for fresh ideas or young startups, this package will help get the business off the ground")
    serv1_div1 = models.CharField(max_length=255, default='Environment and competition')
    serv1_div2 = models.CharField(max_length=255, default='Designing the marketing plan')
    serv1_price = models.CharField(max_length=255, default='$199')


    serv2_title = models.CharField(max_length=255, default='Accelerated Growth')
    serv2_text = models.CharField(max_length=255, default='Use this service pack to give your company the necessary impulse to become an industry leader')
    serv2_div1 = models.CharField(max_length=255, default='Business strategy planning')
    serv2_div2 = models.CharField(max_length=255, default='Taking the planned actions')
    serv2_price = models.CharField(max_length=255, default='$299')
    
    serv3_title = models.CharField(max_length=255, default='Market Domination')
    serv3_text = models.CharField(max_length=255, default='You already are a reference point in your industry now you need to learn about acquisitions')
    serv3_div1 = models.CharField(max_length=255, default='Maintaining the leader status')
    serv3_div2 = models.CharField(max_length=255, default='Acquisitions the right way')
    serv3_price = models.CharField(max_length=255, default='$299')

    test1_text = models.CharField(max_length=300, default='The guys from Aria helped with getting my business off the ground and turning into a profitable company.')
    test1_author = models.CharField(max_length=255, default='Jude Thorn - Founder')

    test2_text = models.CharField(max_length=300, default='I purchased the Growth Accelerator service pack a few years ago and I renewed the contract each year.') 
    test2_author = models.CharField(max_length=255, default='Marsha Singer - Marketer')

    test3_text = models.CharField(max_length=300, default="Aria's CEO personally attends client meetings and gives his feedback on business growth strategies.")
    test3_author = models.CharField(max_length=255, default='Roy Smith - Developer')

    test4_text = models.CharField(max_length=300, default='At the beginning I thought the prices are a little high for what they offer but they over deliver each and every time.')
    test4_author = models.CharField(max_length=255, default='Ronald Spice - Owner')

    test5_text = models.CharField(max_length=300, default='I recommend Aria to every business owner or growth leader that wants to take his company to the next level.')
    test5_author = models.CharField(max_length=255, default="Lindsay Rune - Manager")

    test6_text = models.CharField(max_length=300, default="My goals for using Aria's services seemed high when I first set them but they've met them with no problems.")
    test6_author = models.CharField(max_length=255, default="Ann Black - Consultant")
    
    team1_name = models.CharField(max_length=255, default='John Whitelong')
    team1_title = models.CharField(max_length=255, default='General Manager')

    team2_name = models.CharField(max_length=255, default='Veronique Smith')
    team2_title = models.CharField(max_length=255, default='Business Developer')

    team3_name = models.CharField(max_length=255, default='Chris Zimerman')
    team3_title = models.CharField(max_length=255, default='Online Marketer')

    team4_name = models.CharField(max_length=255, default='Mary Villalonga')
    team4_title = models.CharField(max_length=255, default='Community Manager')

    num1 = models.IntegerField(default=231)
    num2 = models.IntegerField(default=121)
    num3 = models.IntegerField(default=159)

    address = models.CharField(max_length=255, default='22nd Innovative Street, San Francisco, CA 94043, US')
    phone_num1 = models.CharField(max_length=111, default='+81 720 22 126')
    phone_num2 = models.CharField(max_length=111, default='+81 720 22 128')
    email = models.EmailField(max_length=150, default='mailto:office@aria.com')

    def __str__(self):
        return self.title

class ContactRequest(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    interest = models.CharField(max_length=255, null=True, blank=True)
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ContactRequest2(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    