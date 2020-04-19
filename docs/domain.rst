Domain
======

Procesark's main objective is to execute a sequence of **Jobs** wrapped in a
**Process** according to a programmed schedule, a direct web request, a
terminal command or any other kind of **Trigger**.

.. graphviz::

    digraph {
        graph [pad="0.5", nodesep="0.5", ranksep="2"]
        node [shape=plain]
        rankdir=LR

        Job [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td><i>Job</i></td></tr>
        <tr><td port="id">id</td></tr>
        </table>>]

        Process [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td><i>Process</i></td></tr>
        <tr><td port="id">id</td></tr>
        </table>>]

        Allocation [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td><i>Allocation</i></td></tr>
        <tr><td port="process_id">process_id</td></tr>
        <tr><td port="job_id">job_id</td></tr>
        </table>>]

        Trigger [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td><i>Trigger</i></td></tr>
        <tr><td port="id">id</td></tr>
        <tr><td port="process_id">process_id</td></tr>
        </table>>]

        Allocation:process_id -> Process:id
        Allocation:job_id -> Job:id
        Trigger:process_id -> Process:id

        


    }