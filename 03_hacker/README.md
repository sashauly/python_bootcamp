# Day 03 - Python Bootcamp

Fight the system, help the people!

## Table of Contents

- [Day 03 - Python Bootcamp](#day-03---python-bootcamp)
  - [Table of Contents](#table-of-contents)
    - [Rules of the day](#rules-of-the-day)
  - [Tasks](#tasks)
    - [Exercise 00: Preparation (exploit.py, evilcorp.html)](#exercise-00-preparation-exploitpy-evilcorphtml)
    - [Exercise 01: Cash Flow (producer.py, consumer.py)](#exercise-01-cash-flow-producerpy-consumerpy)
    - [Exercise 02: Deploy (gen\_ansible.py)](#exercise-02-deploy-gen_ansiblepy)
    - [Reading and tips](#reading-and-tips)

### Rules of the day

- You should only turn in `*.py` files
- It is encouraged to write some tests for various cases inside your scripts as well. To make them run only when script is executed directly and not imported from somewhere else you can use `if __name__ == "__main__":` statement. You can read more about it [here](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

## Tasks

### Exercise 00: Preparation ([exploit.py](./hacker/exploit.py), [evilcorp.html](./hacker/evilcorp.html))

You can just run `python3 -m http.server` in a directory with this file to be able to test
 our little prank in a browser. Just open `http://127.0.0.1:8000/evilcorp.html` and you'll see the form yourself.

Trenton immediately showed a script on her screen that had to be injected into a web page:

```html
 <script>
        hacked = function() {
            alert('hacked');
        }
        window.addEventListener('load',
          function() {
            var f = document.querySelector("form");
            f.setAttribute("onsubmit", "hacked()");
          },
          false
        );
</script>
```

Let's call this operation... [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)!

-----

You need to write a Python script `exploit.py` that will do several things:

- First, it needs to read a file "evilcorp.html"
- Second, it should modify page title (in `<title>` tags) to be "Evil Corp - Stealing your money every day"
- Third, it should parse out the name of the user from the page (including the pronoun) and inject new tag `<h1>`
  into a `body` of a page, saying `<h1>Mr. Robot, you are hacked!</h1>`, where 'Mr. Robot' is a parsed pronoun
  and name.
- Fourth, it needs to inject a Trenton's script into a `body` of a page as well. If everything is okay, when
  the 'Send' button is pressed, you should see the word "hacked" appearing in an alert window.
- Finally, the link at the bottom of a page should now lead to `https://mrrobot.fandom.com/wiki/Fsociety` with
  an actual name of the company on a page replaced with "Fsociety".

The new HTML file should be named "evilcorp_hacked.html" and placed in the same directory as the source
"evilcorp.html" file.

### Exercise 01: Cash Flow ([producer.py](./hacker/producer.py), [consumer.py](./hacker/consumer.py))

You need to write two scripts - `producer.py` and `consumer.py`.

Producer needs to generate JSON messages like this:

```json
{
   "metadata": {
       "from": 1023461745,
       "to": 5738456434
   },
   "amount": 10000
}
```

and put them as a payload into a [Redis](https://redis.io/) pubsub queue. All account numbers ("from" and "to") should
consist of exactly 10 digits. Additional points can be earned if the code uses builtin `logging`
module (instead of `print` function) to write produced messages to stdout for manual testing.

Consumer should receive an argument with a list of account numbers like this:

```bash
~$ python consumer.py -e 7134456234,3476371234
```

where `-e` is a parameter receiving a list of bad guys' account numbers. When started, it should read
messages from a pubsub queue and print them to stdout on one line each. For accounts from the
"bad guys' list" if they are specified as a receiver consumer should *swap* sender and receiver for
the transaction. But this should happend *only* in case "amount" is not negative.

For example, if producer generates three messages like these:

```json
{"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

consumer started like

```bash
python consumer.py -e 2222222222,4444444444
```

should print out:

```json
{"metadata": {"from": 2222222222,"to": 1111111111},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

Notice that only the first line was changed. Second one wasn't because "amount" was negative (even
though receiver is a bad guy). Third one wasn't changed because bad guy is a sender, not a receiver.

### Exercise 02: Deploy ([gen_ansible.py](./hacker/gen_ansible.py))

To complete this exercise, you don't need to actually know [Ansible](https://docs.ansible.com/ansible/latest/index.html)  in details. It would be nice if
you could test your code through it, even though it's not strictly required. There is a list of
tasks that should be placed in a generated "deploy.yml" file in YAML format:

- Install packages
- Copy over files
- Run files on a remote server with a Python interpreter, specifying corresponding arguments

These tasks should be generated in Ansible notation (e.g. look [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) for notation
on copying files). The script should be named "gen_ansible.py".

Your code should convert "todo.yml" into "deploy.yml" following this notation.

### Reading and tips

Working with HTML is one of the typical tasks when you are writing parsers and various server
code using Python. Two libraries that are most widely used for this are [lxml](https://lxml.de/) and
aforementioned [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). They are not mutually exclusive,
though, as lxml can be used as a parsing backend for BS4, combining great performance with pretty
good API flexibility. You can read about parsing backends [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).

Working with Redis is also a pretty common task to encounter in the world of applied Python.
And it can also be optimized by using an optional [low-level C wrapper](https://github.com/redis/hiredis-py). It is not a necessary
requirement in this task, but still a good module to know about.

Working with YAML is also a very common task, for which [PyYAML](https://pyyaml.org/) is often used. Parsing config
files or writing Ansible plugins is something you can encounter often if Python is used in your
team as a language for dealing with infrastructure. It would require a lot of time and text to
introduce a specific YAML format for this task, that's why an existing standard is chosen here.
Even though it requires a bit of time and effort to study, it can be really helpful to know the
very basics of Ansible for your future job or just daily automation tasks.
