from django.db import models
import datetime

# Create your models here.
class Members(models.Model):
    
    sex = (
        (1,"男"),
        (2,"女")
        )
    
    training_choices = (
        (1, "14日"),
        (2, "21日"),
        (3, "40日"),
        (4, "その他")
    )
    
    training_fees = (
        (1, "完納"),
        (2, "未納")
    )
    
    progress_states = (
        (1, "準備中"),
        (2, "修練中"),
        (3, "退所"),
        (4, "短期滞在"),
        (5, "前泊・延泊")
    )

    name = models.CharField(max_length=100)
    
    gender = models.IntegerField(choices=sex)
        
    birthday = models.DateField(null=True)
    
    enter_day = models.DateField()

    exit_day = models.DateField()
    
    training = models.IntegerField(choices=training_choices)
    
    participation_cost_submit_or_not = models.IntegerField(choices=training_fees)
    
    progress_state = models.IntegerField(choices=progress_states, default=1)
    
    extention_day = models.IntegerField(default = 0)
    
    input_day = models.DateField(null=True)
    
    
    def __str__(self):
        s = "<Member " + \
            "ID: " + str(self.id) + " " + \
            "名前: " + self.name + " " + \
            "性別: " + self.get_gender_display()+ " " + \
            "記載日: " + str(self.input_day) + " " + \
            "入所日: " + str(self.enter_day) + " " + \
            "退所日: " + str(self.exit_day) + " " + \
            "修練区分: " + self.get_training_display() + " " + \
            "参加費の納付: " + self.get_participation_cost_submit_or_not_display() + " " + \
            "進捗状態: " + self.get_progress_state_display() + \
            ">"
            
        return s
