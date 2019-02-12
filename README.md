# Motion detection

The script will detect motion, blink and make some ugly noise from the buzzer.
Clicking the button will turn off the PI.

To run the script on reboot with cron job

``` 
crontab -e
```

```
@reboot python /path/to/motion.py
``` 
